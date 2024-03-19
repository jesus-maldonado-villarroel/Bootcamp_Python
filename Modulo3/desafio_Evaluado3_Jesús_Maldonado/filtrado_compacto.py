
print("Filtrado de umbral por meses \n")
print("Solo se permite ingresar valores numericos\n")

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}
while True:
    try:
        filtro = int(
            input("Ingresa un umbral de dinero mensual para el filtrado: "))
        break
    except ValueError:
        print("Error: Debe ingresar un valor numerico")
ventas_mayores = {mes: ventas[mes] for mes in ventas if ventas[mes] >= filtro}

print(f"Meses con ventas mayores al umbral {filtro}: ")
for mes, venta in ventas_mayores.items():
    print(f"{mes}: {venta}")
