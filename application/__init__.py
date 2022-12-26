from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import User, Users


def create_app(config):
    app = Flask(__name__)  # CRIANDO A APLICAÇÃO
    api = Api(app)  # EXTENDENDO O OBJETO (APP) CRIANDO AS CLASSES (API)
    app.config.from_object(config)
    init_db(app)

    # ADICIONANDO OS ENDPOINTS
    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')
    return app
