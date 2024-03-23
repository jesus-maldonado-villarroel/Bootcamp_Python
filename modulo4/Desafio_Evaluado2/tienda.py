from abc import ABC, abstractmethod
from producto import Producto


class Tienda(ABC):
    @abstractmethod
    def ingresar_productos(self, producto):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass


class TiendaRestaurante(Tienda):
    tipo = "Restaurante"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_productos(self, producto):
        encontrado = False
        for p in self.__productos:
            if p.nombre == producto.nombre:
                encontrado = True
                break

        if not encontrado:
            producto.stock = 0  # Ignorar el stock proporcionado y establecerlo como cero
            self.__productos.append(producto)

    def listar_productos(self):
        if self.__productos:
            retorno = ""
            for producto in self.__productos:
                retorno += f"""
                NOMBRE: {producto.nombre}
                PRECIO: ${producto.precio}
                """
            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                print(
                    f"Venta realizada: {cantidad} unidades de {nombre_producto}")

                return
        print("Producto no encontrado en la tienda.")


class TiendaFarmacia(Tienda):
    tipo = "Farmacia"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_productos(self, producto):
        encontrado = producto in self.__productos
        if not encontrado:
            self.__productos.append(producto)
        else:
            indice = self.__productos.index(producto)
            self.__productos[indice].stock += producto.stock

    def listar_productos(self):
        if self.__productos:
            retorno = ""
            for producto in self.__productos:
                m = ":::Envío gratis al solicitar este producto:::" if producto.precio > 15000 else ""
                retorno += f"""
                NOMBRE: {producto.nombre}
                PRECIO: ${producto.precio}
                {m}
                """
            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(
                        f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print(
                        f"No hay suficiente stock para vender {cantidad} unidades de {nombre_producto}.")
                    print(
                        f"Se venderán {producto.stock} unidades en su lugar.")
                    producto.stock = 0
                return
        print("Producto no encontrado en la tienda.")


class TiendaSupermercado(Tienda):
    tipo = "Supermercado"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_productos(self, producto):
        encontrado = producto in self.__productos
        if not encontrado:
            self.__productos.append(producto)
        else:
            indice = self.__productos.index(producto)
            self.__productos[indice].stock += producto.stock

    def listar_productos(self):
        if self.__productos:
            retorno = ""
            for producto in self.__productos:
                m = f"Alerta: Pocos productos disponibles: {producto.stock}" if producto.stock < 10 else ""
                retorno += f"""
                NOMBRE: {producto.nombre}
                PRECIO: ${producto.precio}
                STOCK: {producto.stock}
                {m}
                """
            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    print(
                        f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print(
                        f"No hay suficiente stock para vender {cantidad} unidades de {nombre_producto}.")
                    print(
                        f"Se venderán {producto.stock} unidades en su lugar.")
                    producto.stock = 0
                return
        print("Producto no encontrado en la tienda.")
