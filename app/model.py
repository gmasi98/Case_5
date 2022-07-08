from .extensions import db

class BaseModel(db.Model):
    # Classe abstrata
    __abstract__ = True 

    # Funções
    @staticmethod
    def delete(obj):
        db.session.delete(obj)
        db.session.commit()

    def save(self):
        db.session.save(self)
        db.session.commit()

    def update(self):
        db.session.commit()
        