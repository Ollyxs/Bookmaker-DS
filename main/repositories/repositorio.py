from .. import db
from main import models


class RepositorioService():
    def __init__(self, modelo):
        self.__modelo = modelo

    def obtener_todos(self):
        objetos = db.session.query(self.__modelo).all()
        return objetos

    def obtener_por_id(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        return objeto

    def crear(self, objeto):
        db.session.add(objeto)
        db.session.commit()
        return objeto

    def eliminar(self, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        db.session.delete(objeto)
        db.session.commit()

    def modificar(self, data, id):
        objeto = db.session.query(self.__modelo).get_or_404(id)
        for key, value in data:
            setattr(objeto, key, value)
        db.session.add(objeto)
        db.session.commit()
        return objeto
