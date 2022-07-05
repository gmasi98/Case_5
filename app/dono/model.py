from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

dono_api = Blueprint("dono_api", __name__)

class Dono(BaseModel):

    __tablename__ = "dono"

    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos para a pag do dono
    '''nome = db.Column(db.String(100))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    data_consulta = db.Column(db.Date(12))'''