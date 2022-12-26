# CONFIGURAÇÃO DO BANCO DE DADOS

from flask_mongoengine import MongoEngine  # IMPORTANDO MONGOENGINE


db = MongoEngine()  # CLASSE DB


def init_db(app):
    db.init_app(app)
