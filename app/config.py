class Config:
    # onde está o banco de dados
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True