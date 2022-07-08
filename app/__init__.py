from flask import Flask 
from .extensions import db, migrate, mail,jwt
from .config import Config
from app.cliente.model import cliente_api
from app.dono.model import dono_api
from app.funcionario.model import funcionario_api
from app.insumos.model import insumos_api
from app.cliente.routes import cliente_api
from app.dono.routes import cliente_api
from app.funcionario.routes import funcionario_api
from app.insumos.routes import insumos_api




def create_app():
    app = Flask(__name__)
    # configura app
    app.config.from_object(Config)
    
    # banco de dados sendo inicializado no app
    db.init_app(app)
    # migrate inicializado no app de acordo com o banco de dados
    migrate.init_app(app, db)
    # mail sendo inicializado no app
    mail.init_app(app)
    jwt.init_app(app)


    # aqui eh pra registrar no banco de dados
    app.register_blueprint(cliente_api)
    app.register_blueprint(dono_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(insumos_api)

    return app