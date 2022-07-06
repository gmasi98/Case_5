from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

cliente_api = Blueprint("cliente_api", __name__)

class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)

    # Dentro de uma tabela user, temos muitos atributos: login, senha, telefone, email, 
    nome = db.Column(db.String(100))
    idade = db.Column(db.String(3))
    data_nascimento = db.Column(db.String(10))
    endereco= db.Column(db.String(100))
    cpf = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))
    telefone = db.Column(db.String(11))
    data_consulta = db.Column(db.String(11))

    # Relacionamentos
    marcela_dono = db.Column(db.Integer, db.ForeignKey("dono.id"))


    
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
            "senha": self.senha,
            "telefone": self.telefone,
            "data_consulta": self.data_consulta
            # não faz sentido retornar o json de uma relação de tabelas, por exemplo
        }

