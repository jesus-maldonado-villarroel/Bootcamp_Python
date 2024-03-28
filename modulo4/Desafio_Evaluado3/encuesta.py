from pregunta import Pregunta


class Encuesta():
    def __init__(self, nombre: str, preguntas: list):
        self.nombre = nombre
        self.__preguntas = [
            Pregunta(
                p["enunciado"],
                p["ayuda"],
                p["alternativas"],
                p["requerido"],
            ) for p in preguntas
        ]

        self.__listados_respuestas = []

    def mostrar_encuesta(self):
        print(self.nombre)

        for p in self.__preguntas:
            p.mostrar_pregunta()

    def agregar_listado_respuesta(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list, edad_min: int, edad_max: int):
        super().__init__(nombre, preguntas)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self):
        return self.__edad_min

    @edad_min.setter
    def edad_min(self, nueva_edad_min):
        self.__edad_min = nueva_edad_min

    @property
    def edad_max(self):
        return self.__edad_max

    @edad_max.setter
    def edad_max(self, nueva_edad_max):
        self.__edad_max = nueva_edad_max

    def agregar_respuesta(self, respuestas: list):
        if self.__edad_min <= respuestas.usuario.edad <= self.__edad_max:
            super().agregar_listado_respuestas(respuestas)


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list, region: list):
        super().__init__(nombre, preguntas)
        self.region = region

    def agregar_respuesta(self, respuestas: list):
        if self.region == respuestas.usuario.region:
            super().agregar_listado_respuestas(respuestas)
