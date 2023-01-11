import os


# CONECTANDO O BANCO, CONFIGURAÇÃO DA API
class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USER'),
        'password': os.getenv('MONGODB_PASSWORD')
    }


class ProdConfig:

    MONGODB_USER = os.getenv('MONGODB_USER')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    MONGODB_DB = os.getenv('MONGODB_DB')

    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://%s:%s@%s/%s?retryWrites=true&w=majority' % (
            MONGODB_USER,
            MONGODB_PASSWORD,
            MONGODB_HOST,
            MONGODB_DB
        )
    }


class MockConfig:

    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongomock://localhost',
    }
