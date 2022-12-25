# IMPORTANDO AS TECNOLOGIAS
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine

# CRIANDO A APLICAÇÃO
app = Flask(__name__)

# CONECTANDO O BANCO .CONFIG
app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'

}

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )

api = Api(app)  # EXTENDENDO O OBJETO (APP) CRIANDO AS CLASSES (API)
db = MongoEngine(app)  # CLASSE DB

# CONECTANDO O BANCO .CONFIG
app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': 'admin',
    'password': 'admin'

}


# DECLARAÇÃO DA CLASSE QUE VAI SE COMUNICAR COM O BANCO
#  MODELO DE INTERAÇÃO COM O BD
class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


# CONFIGURAÇÕES DO RESTFUL, TODOS ENDPOINT'S TEM UMA CLASSE
class Users(Resource):
    def get(self):
        return {"message": "user1"}


class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        UserModel(**data).save()

    def get(self, cpf):
        return {"message": "CPF"}


# ADICIONANDO OS ENDPOINTS
api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

# EXECUÇÃO DO SCRIPT COM HOST 0.0.0.0 P NAO TER ERRO DE CONEXAO DEFUSED
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
