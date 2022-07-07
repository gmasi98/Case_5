# guardar arq sensíveis do usuario
class Sensive:
    # onde está o banco de dados
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JSON_SORT_KEYS = False

    # Problema a ser solucionado, sendGrid
    '''MAIL_SERVER = ""
    MAIL_PORT = ""
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False'''

sen = Sensive()