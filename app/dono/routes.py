from flask import Blueprint
from app.dono.model import dono_api
from app.dono.controller import DonoCreate, DonoDetails,Login
dono_api = Blueprint('cliente_api',__name__)

# registrando cliente

dono_api.add_url_rule('/criar', view_func=DonoCreate.as_view("cria dono"), methods=['POST', 'GET'])
dono_api.add_url_rule('/alterar', view_func=DonoDetails.as_view("modifica dono"), methods=['GET', 'PATCH', 'DELETE'])
dono_api.add_url_rule('/login_dono', view_func = Login.as_view('login_dono'), methods=['POST'])