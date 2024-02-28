#ejercicio numero 2
print("ejercicio numero 2: ")
print("Velocidad de escape")
print("...................................")
print("Ingrese los valores que se requieren ")
print("...................................")
print("SOLO INGRESAR VALORES NUMERICOS PARA UN CORRECTO FUNCIONAMIENTO")

P = float(input("Ingresa el valor de la suscripcion: "))
U = float(input("Ingresa la cantidad de usuarios: "))
GT = float(input("Ingresa el gasto total: "))

Utilidades = P * U - GT

print(f'Las utilidades del proyecto: $ {Utilidades} Dolares')