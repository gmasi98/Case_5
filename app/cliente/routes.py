from flask import Blueprint
from app.cliente.model import cliente_api
from app.cliente.controller import ClienteCreate, ClienteDetails,Login
cliente_api = Blueprint('cliente_api',__name__)

# registrando cliente

cliente_api.add_url_rule('/cadastrar', view_func=ClienteCreate.as_view("cadastra cliente"), methods=['POST', 'GET'])
cliente_api.add_url_rule('/modificar', view_func=ClienteDetails.as_view("modifica cliente"), methods=['GET', 'PATCH', 'DELETE'])
cliente_api.add_url_rule('/login', view_func = Login.as_view('login'), methods=['POST'])