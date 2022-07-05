from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# inicializa o banco de dados
db = SQLAlchemy()
# inicializa migrate
migrate = Migrate()