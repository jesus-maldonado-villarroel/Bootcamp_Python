class ListadoRespuestas():
    def __init__(self, respuestas: list):
        self.__respuestas = respuestas

    def agregar_respuesta(self, respuesta):
        self.__respuestas.append(respuesta)

    def obtener_respuestas(self):
        return self.__respuestas
