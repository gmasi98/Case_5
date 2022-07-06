from app.cliente.model import cliente_api
from app.cliente.controller import ClienteCreate, ClienteDetails

# registrando cliente
cliente_api.add_url_rule('/registro', view_func=ClienteCreate.as_view("cria cliente"), methods=['POST', 'GET'])
cliente_api.add_url_rule('/modificar', view_func=ClienteDetails.as_view("cria cliente"), methods=['GET', 'PATCH', 'DELETE'])

