from .. import db
from sqlalchemy.ext.hybrid import hybrid_property


class Cliente(db.Model):
    __tablename__ = "clientes"
    __id = db.Column('id', db.Integer, primary_key=True)
    __apellido = db.Column('apellido', db.String(50), nullable=False)
    __nombre = db.Column('nombre', db.String(50), nullable=False)
    __email = db.Column('email', db.String(120), nullable=False)
    __activado = db.Column('activado', db.Boolean, nullable=False)


    def __repr__(self):
        return '<Cliente: %r %r>' % (self.__id, self.__email)

    @hybrid_property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @id.deleter
    def id(self):
        del self.__id

    @hybrid_property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido

    @apellido.deleter
    def apellido(self):
        del self.__apellido

    @hybrid_property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @hybrid_property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @email.deleter
    def email(self):
        del self.__email

    @hybrid_property
    def activado(self):
        return self.__activado

    @activado.setter
    def activado(self, activado):
        self.__activado = activado

    @activado.deleter
    def activado(self):
        self.__activado
