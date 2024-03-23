from tienda import TiendaFarmacia, TiendaRestaurante, TiendaSupermercado
from producto import Producto


def main():
    nombre_tienda = input("Ingrese el nombre de su tienda: ")
    costo_delivery = float(input("Ingrese costo del delivery: "))

    tipo_tienda = int(input(f"""Ingrese el tipo de su tienda 
                        1.Farmacia 
                        2.Restaurante 
                        3.Supermercado 
                        
    Selecciona tu opcion: """))

    if tipo_tienda == 1:
        tienda = TiendaFarmacia(nombre_tienda, costo_delivery)
    elif tipo_tienda == 2:
        tienda = TiendaRestaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda == 3:
        tienda = TiendaSupermercado(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido")
        return

    while True:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        stock_producto = int(input("Ingrese el stock del producto: "))

        producto = Producto(nombre_producto, precio_producto, stock_producto)
        tienda.ingresar_productos(producto)

        continuar = input("¿Desea continuar? (si/no): ")
        if continuar.lower() != "si":
            break

    while True:
        opcion = int(input(f"""
                        1. Listar productos
                        2. Realizar venta
                        3. Salir
    
    Seleccione una opción: """))

        if opcion == 1:
            print(tienda.listar_productos())

        elif opcion == 2:
            nombre_producto = input(
                "Ingrese el nombre del producto para la venta: ")
            cantidad = int(input("Ingrese la cantidad para la venta: "))
            tienda.realizar_venta(nombre_producto, cantidad)

        elif opcion == 3:
            print("Gracias por utilizar nuestra app")
            break
        else:
            print("Opción inválida, ingrese una opción válida")


if __name__ == "__main__":
    main()
