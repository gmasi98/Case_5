from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_jwt_extended import JWTManager

# inicializa o banco de dados
db = SQLAlchemy()
# inicializa migrate
migrate = Migrate()
# para email
mail = Mail()

jwt =JWTManager()