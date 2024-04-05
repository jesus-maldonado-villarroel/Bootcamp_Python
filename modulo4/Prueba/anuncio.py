from abc import ABC, abstractmethod


class Anuncio(ABC):
    SUB_TIPOS = ()

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, nuevo_ancho):
        self.__ancho = nuevo_ancho if nuevo_ancho > 0 else 1

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, nuevo_alto):
        self.__alto = nuevo_alto if nuevo_alto > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, nuevo_url_archivo):
        self.__url_archivo = nuevo_url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, nuevo_url_clic):
        self.__url_clic = nuevo_url_clic

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if nuevo_sub_tipo in self.sub_tipo:
            self._sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoException(
                f"El Subtipo indicado no está permitido para este formato: {nuevo_sub_tipo}")

    @staticmethod
    def mostrar_formatos():
        print("FORMATO 1:")
        print("==========")
        for sub_tipo in Anuncio.SUB_TIPOS:
            print(f"- {sub_tipo}")

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass


class Video(Anuncio):
    SUB_TIPOS = ('instream', 'outstream')
    FORMATO = "Video"

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, nueva_duracion):
        self.__duracion = nueva_duracion if nueva_duracion > 0 else 5

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if nuevo_sub_tipo in self.SUB_TIPOS:
            self._sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoException(
                f"El Subtipo indicado no está permitido para este formato Video: {nuevo_sub_tipo}")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    SUB_TIPOS = ('tradicional', 'native')
    FORMATO = "Display"

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if nuevo_sub_tipo in self.SUB_TIPOS:
            self._sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoException(
                f"El Subtipo indicado no está permitido para este formato Display: {nuevo_sub_tipo}")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    SUB_TIPOS = ('facebook', 'linkedin')
    FORMATO = "Social"

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, nuevo_sub_tipo):
        if nuevo_sub_tipo in self.SUB_TIPOS:
            self._sub_tipo = nuevo_sub_tipo
        else:
            raise SubTipoInvalidoException(
                f"El Subtipo indicado no está permitido para este formato Social: {nuevo_sub_tipo}")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")


class SubTipoInvalidoException(Exception):
    pass
