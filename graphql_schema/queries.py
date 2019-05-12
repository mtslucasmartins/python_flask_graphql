import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from graphql_schema.objects import PostObject, UserObject

from models import Post


class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()

    find_post = graphene.Field(
        lambda: graphene.List(PostObject),
        uuid=graphene.Int(),
        page_index=graphene.Int(),
        page_size=graphene.Int()
    )

    user = graphene.Field(UserObject, uuid=graphene.Int())

    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)

    def resolve_find_post(self, info, **args):
        post_query = PostObject.get_query(info)

        uuid = args.get('uuid')
        page_index = args.get('page_index', 0)
        page_size = args.get('page_size', 10)

        # pagination...
        post_query = post_query.offset(page_index * page_size) \
                               .limit(page_size)

        # filters...
        if uuid is not None:
            post_query = post_query.filter(Post.uuid == uuid)

        return post_query

    def resolve_user(self, info, **args):
        query = UserObject.get_query(info)
        uuid = args.get('uuid')
        return query.get(uuid)
