from app.insumos.model import insumos_api
from app.insumos.controller import InsumosCreate, InsumosDetails

# registrando cliente
insumos_api.add_url_rule('/registro', view_func=InsumosCreate.as_view("cria insumo"), methods=['POST', 'GET'])
insumos_api.add_url_rule('/modificar', view_func=InsumosDetails.as_view("modifica insumo"), methods=['GET', 'PATCH', 'DELETE'])
