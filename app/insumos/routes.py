from app.insumos.model import insumos_api
from app.insumos.controller import InsumosCreate, InsumosDetails

# registrando cliente
insumos_api.add_url_rule('/registro', view_func=InsumosCreate.as_view("cria cliente"), methods=['POST', 'GET'])
insumos_api.add_url_rule('/modificar', view_func=InsumosDetails.as_view("cria cliente"), methods=['GET', 'PATCH', 'DELETE'])

