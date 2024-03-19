from te import Te


def main():
    # Pedir al usuario el te que desea tomar
    sabor = int(input(
        "Ingrese el sabor del té \n 1: Té negro \n 2: Té verde \n 3: Agua de hierbas \n Seleccione su sabor: "))
    tamaño = int(input(
        "Ingrese el formato del té \n 1: 300 gr \n 2: 500 gr \n Seleccione el tamaño: "))

    # trayendo el tiempo, la recomendación y el precio desde la clase Te
    tiempo_preparacion, recomendacion = Te.duracion_preparacion_y_recomendacion(
        sabor)
    precio = Te.precio_por_tamaño(tamaño)

    # Detalle del pedido
    print("\nDetalle del pedido:")
    print("Sabor del té:", "Té negro" if sabor == 1 else (
        "Té verde" if sabor == 2 else "Agua de hierbas"))
    print("Formato:", "300 gramos" if tamaño == 1 else (
        "500 gramos" if tamaño == 2 else ("NO EXISTE ESE FORMATO")))
    print("Precio:", precio)
    print("Tiempo de preparación:", tiempo_preparacion, "minutos")
    print("Recomendación:", recomendacion)


if __name__ == "__main__":
    main()
