
class Te:
    duracion = 365
    tamaño_300_gramos = 1
    tamaño_500_gramos = 2
    precio_300_gramos = 3000
    precio_500_gramos = 5000

    @staticmethod
    def duracion_preparacion_y_recomendacion(sabor):
        tiempo_preparacion = ""
        recomendacion = ""
        if sabor == 1:  # Té negro
            tiempo_preparacion = 3
            recomendacion = "Se recomienda consumir al desayuno."
        elif sabor == 2:  # Té verde
            tiempo_preparacion = 5
            recomendacion = "Se recomienda consumir al medio día."
        elif sabor == 3:  # Agua de hierbas
            tiempo_preparacion = 6
            recomendacion = "Se recomienda consumir al atardecer."
        return tiempo_preparacion, recomendacion

    @staticmethod
    def precio_por_tamaño(tamaño):
        if tamaño == Te.tamaño_300_gramos:
            return Te.precio_300_gramos
        elif tamaño == Te.tamaño_500_gramos:
            return Te.precio_500_gramos
        else:
            return "No existe otro tamaño"
