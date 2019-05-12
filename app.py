# Imports
from flask import Flask
from flask_graphql import GraphQLView

from config import HOST, PORT
from database import db
from graphql_schema import schema

# app initialization
app = Flask(__name__)
app.config.from_object('default_settings')

# Configs
# TO-DO

# Modules
db.init_app(app)

# Routes
@app.before_first_request
def create_tables():
    print('Creating Tables...')
    db.create_all()


@app.route('/')
def index():
    return '<p> Welcome </p>'


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
