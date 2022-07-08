from app.sensive import sen
class Config:
    # onde está o banco de dados
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    JSON_SORT_KEYS = False

    # aplicação sendgrid, pode ser uma possível fonte de erros, 
    # não consegui utilizar a plataforma por falta de autorização por parte da mesma
    # assim não consegui pegar alguns atributos essenciais para o correto funcionamento do código

    JWT_SECRET_KEY = "ERQTYUIODFGHJKCVBNMFFDHJSKYDEIQWSOKEDUQJWI"

    # aplicações send
    MAIL_SERVER = sen.MAIL_SERVER
    MAIL_PORT = sen.MAIL_PORT
    MAIL_USERNAME = sen.MAIL_USERNAME
    MAIL_PASSWORD = sen.MAIL_PASSWORD
    MAIL_USE_TLS = sen.MAIL_USE_TLS
    MAIL_USE_SSL = sen.MAIL_USE_SSL
