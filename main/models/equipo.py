from .. import db


class Equipo(db.Model):
    __tablename__ = "equipos"
    __id = db.Column(db.Integer, primary_key=True)
    __nombre = db.Column(db.String(50), nullable=False)
    __escudo = db.Column(db.String(50), nullable=False)
    __email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Eqipo: %r %r>' % (self.__id, self.__email)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def escudo(self):
        return self.__escudo

    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo

    @escudo.deleter
    def escudo(self):
        del self.__escudo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email
