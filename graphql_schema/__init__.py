import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from graphql_schema.queries import Query
from graphql_schema.mutations import Mutation


schema = graphene.Schema(query=Query, mutation=Mutation)
