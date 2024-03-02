print("Calcule Su Indice De Masa Corporal")
print("------------------------------------\n")

W = float(input("Ingresa tu peso en KG: "))
H = float(input("ingresa tu altura en centimetros: "))

H = H / 100

IMC = W / (H**2)

if IMC < 18.5:
    print(f'Su IMC es: {round(IMC, 2)}')
    print("La clasificación de la OMS es Bajo Peso")
elif IMC <= 18.5 or IMC < 25:
    print(f'Su IMC es: {round(IMC, 2)}')
    print("La clasificación de la OMS es Adecuado")
elif IMC <= 25 or IMC < 30:
    print(f'Su IMC es: {round(IMC, 2)}')
    print("La clasificación de la OMS es Sobrepeso")
elif IMC <= 30 or IMC < 35:
    print(f'Su IMC es: {round(IMC, 2)}')
    print("La clasificación de la OMS es Obesidad Grado I")
elif IMC <= 35 or IMC < 40:
    print(f'Su IMC es: {round(IMC, 2)}')
    print("La clasificación de la OMS es Obesidad Grado II")
elif IMC >= 40:
    print(f'Su IMC es: {round(IMC, 2)}')
    print("La clasificación de la OMS es Obesidad Grado III")
