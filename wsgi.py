from application import create_app
import os


# CRIANDO CONDIÇÃO DE INICIALIZACAO, COM AMBIENTE DO COMPOSE
if os.getenv('FLASK_ENV') == "development":
    app = create_app('config.DevConfig')
else:
    app = create_app('config.ProdConfig')

# EXECUÇÃO DO SCRIPT COM HOST 0.0.0.0 P NAO TER ERRO DE CONEXAO DEFUSED
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
