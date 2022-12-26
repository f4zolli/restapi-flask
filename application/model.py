from .db import db


# DECLARAÇÃO DA CLASSE QUE VAI SE COMUNICAR COM O BANCO
#  MODELO DE INTERAÇÃO COM O BD
class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)
