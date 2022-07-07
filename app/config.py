from app.sensive import sen
class Config:
    # onde está o banco de dados
    SQLALCHEMY_DATABASE_URI = sen.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JSON_SORT_KEYS = False

    # Problema a ser solucionado, sendGrid
    '''MAIL_SERVER = "sen.MAIL_SERVER"
    MAIL_PORT = "sen.MAIL_PORT"
    MAIL_USERNAME = "sen.MAIL_USERNAME"
    MAIL_PASSWORD = "sen.MAIL_PASSWORD"
    MAIL_USE_TLS = sen.MAIL_USE_TLS
    MAIL_USE_SSL = sen.MAIL_USE_SSL'''
