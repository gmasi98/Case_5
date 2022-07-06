from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    # Dentro de uma tabela user, temos muitos atributos: login, senha, telefone, email, 
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(20))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(11))
    data_consulta = db.Column(db.String(11))

    def json(self):

        return {
            # aqui vão os atributos da classe
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "data_consulta": self.data_consulta
            # não faz sentido retornar o json de uma relação de tabelas, por exemplo
        }

