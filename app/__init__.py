from flask import Flask 
from .extensions import db, migrate
from .config import Config
# aqui eh pra importar os modelos
from app.cliente.model import cliente_api
#from app.dono.model import dono_api
#from app.funcionario import funcionario_api

def create_app():
    app = Flask(__name__)
    # configura app
    app.config.from_object(Config)
    
    # banco de dados sendo inicializado no app
    db.init_app(app)
    # migrate inicializado no app de acordo com o banco de dados
    migrate.init_app(app, db)

    # aqui eh pra registrar no banco de dados
    app.register_blueprint(cliente_api)
    #app.register_blueprint(dono_api)
    #app.register_blueprint(funcionario_api)

   
    return app