from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

funcionario_api = Blueprint("funcionario_api", __name__)

class Funcionario(BaseModel):

    __tablename__ = "funcionario"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100))
    idade = db.Column(db.String(2)) 
    data_nascimento = db.Column(db.String(10))
    cpf = db.Column(db.String(11))
    telefone = db.Column(db.String(11))
    endereco = db.Column(db.String(100))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))
    
    # Relações 

