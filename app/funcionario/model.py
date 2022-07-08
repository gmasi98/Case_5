from app.extensions import db
from app.model import BaseModel
from flask import Blueprint
import bcrypt


funcionario_api = Blueprint("funcionario_api", __name__)

class Funcionario(BaseModel):

    __tablename__ = "funcionario"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100),nullable=False)
    idade = db.Column(db.String(2),nullable=False) 
    data_nascimento = db.Column(db.String(10),nullable=False)
    cpf = db.Column(db.String(11),unique=True,nullable=False)
    telefone = db.Column(db.String(11),nullable=False)
    endereco = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    senha = db.Column(db.String(10),unique=True,nullable=False)
    senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt()).decode()

def json(self):

        return {

            # aqui vão os atributos da classe
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "data_nascimento": self.data_nascimento,
            "endereco": self.endereco,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone
            # não faz sentido retornar o json de uma relação de tabelas, por exemplo
        }