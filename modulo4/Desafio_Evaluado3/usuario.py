from listado_respuestas import ListadoRespuestas


class Usuario():
    def __init__(self, correo: str, edad: int, region: int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        self.__correo = nueva_edad

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, nueva_region):
        self.__region = nueva_region

    def contestar_encuesta(self, respuestas: list):
        listado_respuestas = ListadoRespuestas(respuestas)
        return listado_respuestas
