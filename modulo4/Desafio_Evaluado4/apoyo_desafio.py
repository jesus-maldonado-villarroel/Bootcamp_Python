from error import DimensionError


class Foto():
    MAX = 2500

    def __init__(self, ancho: int, alto: int, ruta: str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        if ancho <= 0 or ancho > 2500:
            raise DimensionError(
                f"El ancho de la foto debe ser mayor a cero y con un maximo de 2500.", ancho, 2500)
        self.__ancho = ancho

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, alto: int) -> None:
        if alto <= 0 or alto > 2500:
            raise DimensionError(
                f"El alto de la foto debe ser mayor a cero y con un maximo de 2500", alto, 2500)
        self.__alto = alto


# f = Foto(50, 500, "LOLA")
# f.ancho = 20000
