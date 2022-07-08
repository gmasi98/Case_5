from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

insumos_api = Blueprint("insumos_api", __name__)

class Insumos(BaseModel):

    __tablename__ = "insumos"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100),nullable=False)
    codigo = db.Column(db.String(2),unique=True,nullable=False) 
    data_validade = db.Column(db.String(10),nullable=False)
    preco = db.Column(db.String(11),nullable=False)

    
    funcionarios = db.relationship("Funcionario", secondary="insumos_funcionario", backref="insumos_verificados_funcionarios")


class InsumosFuncionario(BaseModel):

    __tablename__ = "insumos_funcionario"

    id = db.Column(db.Integer, primary_key=True)

    funcionarios = db.Column(db.Integer, db.ForeignKey("funcionario.id"))

def json(self):

        return {
            # aqui vão os atributos da classe
            "id": self.id,
            "nome": self.nome,
            "codigo": self.codigo,
            "data_validade": self.data_validade,
            "preco": self.preco
            # não faz sentido retornar o json de uma relação de tabelas, por exemplo
        }

