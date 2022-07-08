from app.extensions import db
from app.model import BaseModel
from flask import Blueprint
import bcrypt


dono_api = Blueprint("dono_api", __name__)

class Dono(BaseModel):

    __tablename__ = "dono"

    id = db.Column(db.Integer, primary_key=True)
    
    # Atributos para o dono
    nome = db.Column(db.String(100),unique=True,nullable=False)
    telefone = db.Column(db.String(11),unique=True,nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    senha = db.Column(db.String(10),unique=True,nullable=False)
    senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt()).decode()
    
    # Relações
    clientes = db.relationship("Cliente", backref='dono')

def json(self):

        return {

            # aqui vão os atributos da classe
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
            # não faz sentido retornar o json de uma relação de tabelas, por exemplo
        }