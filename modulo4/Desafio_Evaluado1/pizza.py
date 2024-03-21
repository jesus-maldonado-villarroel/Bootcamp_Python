from ingredientes import Ingredientes


class Pizza:
    def __init__(self):
        self.ingrediente_proteico = ""
        self.ingredientes_vegetales = []
        self.tipo_masa = ""
        self.es_valida = ""
        self.tamaño = "Familiar"
        self.Precio = 10000

    @staticmethod
    def es_valido(elemento, lista_valores_posibles):
        return elemento in lista_valores_posibles

    def realizar_pedido(self):
        self.ingrediente_proteico = input(
            "Ingrese el ingrediente proteico: ").lower()
        self.ingredientes_vegetales.append(
            input("Ingrese el primer ingrediente vegetal: ").lower())
        self.ingredientes_vegetales.append(
            input("Ingrese el segundo ingrediente vegetal: ").lower())
        self.tipo_masa = input("Ingrese el tipo de masa: ").lower()

        self.es_valida = all([
            self.es_valido(self.ingrediente_proteico,
                           Ingredientes.ingredientes_proteico),
            self.es_valido(
                self.ingredientes_vegetales[0], Ingredientes.ingredientes_vegetales),
            self.es_valido(
                self.ingredientes_vegetales[1], Ingredientes.ingredientes_vegetales),
            self.es_valido(self.tipo_masa, Ingredientes.tipos_masa)
        ])
