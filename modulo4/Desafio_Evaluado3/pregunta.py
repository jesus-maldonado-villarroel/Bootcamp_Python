from alternativa import Alternativa


class Pregunta():
    def __init__(self, enunciado: str, ayuda: str, alternativas: list, requerido: bool):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.alternativas = [Alternativa(
            a["Contenido"], a["ayuda"]) for a in alternativas]
        self.requerido = requerido

    def mostrar_pregunta(self):
        print(f'Pregunta: {self.enunciado}')
        if self.ayuda:
            print(f'Ayuda: {self.ayuda}')

        for a in self.__alternativas:
            a.mostrar_altertativa()
