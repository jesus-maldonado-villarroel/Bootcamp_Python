#ejercicio numero 2
print("ejercicio numero 2: ")
print("Velocidad de escape")
print("...................................")
print("Ingrese los valores que se requieren ")
print("...................................")
print("SOLO INGRESAR VALORES NUMERICOS PARA UN CORRECTO FUNCIONAMIENTO")

P = float(input("Ingresa el valor de la suscripcion: "))
U = float(input("Ingresa la cantidad de usuarios: "))
Ut = float(input("Ingresa las utilidades del año pasado: "))
GT = float(input("Ingresa el gasto total: "))

Utilidades = P * U - GT

print(f'Las utilidades del proyecto de este año son: $ {Utilidades} dolares')

Diferencia_Utilidades = Utilidades - Ut

if Diferencia_Utilidades > 0:
    print(f'En comparacion al año pasado tenemos un total de ganancias de: $ {round(Diferencia_Utilidades,2)} Dolares')
else:
    print(f'En comparacion al año pasado tenemos un total de perdidas de: $ {round(Diferencia_Utilidades,2)} Dolares')