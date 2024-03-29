from app.extensions import db
from app.extensions import db
from app.model import BaseModel
from flask import Blueprint
import bcrypt

cliente_api = Blueprint("cliente_api", __name__)

class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True)
    # Atributos
    nome = db.Column(db.String(100),nullable=False)
    idade = db.Column(db.String(3),nullable=False)
    data_nascimento = db.Column(db.String(10),nullable=False)
    endereco= db.Column(db.String(100),nullable=False)
    cpf = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    senha = db.Column(db.String(10),unique=True,nullable=False)
    senha = bcrypt.hashpw(senha.encode(),bcrypt.gensalt()).decode()

    telefone = db.Column(db.String(11),nullable=False)
    data_consulta = db.Column(db.String(11),nullable=False)
    hora_da_consulta = db.Column(db.String(5),nullable=False)

    # Relacionamentos
    marcela_dono = db.Column(db.Integer, db.ForeignKey("dono.id"))


    # retorna as info de um cliente no formato json
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
            "telefone": self.telefone,
            "data_consulta": self.data_consulta,
            "hora_da_consulta": self.hora_da_consulta
            # não faz sentido retornar o json de uma relação de tabelas, por exemplo
        }

