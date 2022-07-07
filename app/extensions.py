from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

# inicializa o banco de dados
db = SQLAlchemy()
# inicializa migrate
migrate = Migrate()
# para email
mail = Mail()