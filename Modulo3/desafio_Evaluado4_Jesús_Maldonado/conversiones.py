from sys import argv

moneda_peruana = argv[1]
moneda_argentina = argv[2]
moneda_americana = argv[3]
moneda_chilena = argv[4]

try:
    moneda_peruana = float(moneda_peruana)
    moneda_argentina = float(moneda_argentina)
    moneda_americana = float(moneda_americana)
    moneda_chilena = int(moneda_chilena)
    conversion_1 = moneda_peruana * moneda_chilena
    print(f"Los {moneda_chilena} Pesos equivalen a: ")
    print(f"{conversion_1} Soles")
    conversion_2 = moneda_argentina * moneda_chilena
    print(f"{conversion_2} Pesos Argentinos")
    conversion_3 = moneda_americana * moneda_chilena
    print(f"{conversion_3} Dolares")
except:
    print("Ingresa valores numericos porfavor estimado usuario: ")

monedas_conversion = {
    "Sol peruano": moneda_peruana,
    "Peso argentino": moneda_argentina,
    "Dolar americano": moneda_americana,
    "Peso chileno": moneda_chilena
}
print("Estas son las monedas ingresadas\n")
print(monedas_conversion)
