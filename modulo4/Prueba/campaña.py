from anuncio import Anuncio, Video, Display, Social
from error import LargoExcedidoException
from datetime import date


class Campaña():
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios: list):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = anuncios

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) <= 250:
            self._nombre = nuevo_nombre
        else:
            raise LargoExcedidoException("El nombre excede los 250 caracteres")

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        cant_video = 0
        cant_display = 0
        cant_social = 0

        for elemento in self.__anuncios:
            if isinstance(elemento, Video):
                cant_video += 1
            elif isinstance(elemento, Display):
                cant_display += 1
            elif isinstance(elemento, Social):
                cant_social += 1
        return f"""
        Nombre de la campaña: {self.nombre}
        Anuncios: {cant_video} Videos, {cant_display} Display, {cant_social} Social
        """


class LargoExcedidoException(Exception):
    pass
