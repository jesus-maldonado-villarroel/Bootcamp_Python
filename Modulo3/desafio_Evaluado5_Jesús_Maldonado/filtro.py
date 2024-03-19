from sys import argv


def filtro(umbral, precios, comparacion="mayor"):
    filtro = {}
    if comparacion == "menor":
        for producto, precio in precios.items():
            if precio < umbral:
                filtro[producto] = precio
    elif comparacion == "mayor":
        for producto, precio in precios.items():
            if precio > umbral:
                filtro[producto] = precio
    else:
        print("Lo sentimos, no es una operacion valida")
    return filtro


precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

if len(argv) < 2:
    print("Debes ingresar un umbral para filtrar los productos.")
    exit()

valor_ingresado = int(argv[1])

comparacion = "mayor" if len(argv) == 2 else argv[2].lower()
productos = filtro(valor_ingresado, precios, comparacion)

if comparacion == "menor":
    print("Productos con precio menor a", valor_ingresado, ":")
elif comparacion == "mayor":
    print("Productos con precio mayor a", valor_ingresado, ":")

for producto, precio in productos.items():
    print(producto, "-", precio)
