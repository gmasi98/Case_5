from flask import Blueprint
from app.cliente.model import funcionario_api
from app.cliente.controller import FuncionarioCreate, FuncionarioDetails,Login
funcionario_api = Blueprint('cliente_api',__name__)

# registrando funcionario

funcionario_api.add_url_rule('/inscricao', view_func=FuncionarioCreate.as_view("inscreve funcionario"), methods=['POST', 'GET'])
funcionario_api.add_url_rule('/mudar', view_func=FuncionarioDetails.as_view("muda funcionario"), methods=['GET', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/login_funcionario', view_func = Login.as_view('login_do_funcionario'), methods=['POST'])