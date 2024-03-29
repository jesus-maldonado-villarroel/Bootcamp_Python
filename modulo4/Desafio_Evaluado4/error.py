class Error(Exception):
    pass


class DimensionError(Error):
    def __init__(self, mensaje: str, dimension: int, maximo: int = None):
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.mensaje and self.dimension and self.maximo:
            return f"DimensionError: {self.mensaje}. Dimension: {self.dimension}, Maximo: {self.maximo}."
        elif self.mensaje and self.dimension:
            return f"DimensionError: {self.mensaje}. Dimension: {self.dimension}."
        elif self.mensaje:
            return f"DimensionError: {self.mensaje}."
        else:
            return super().__str__()
