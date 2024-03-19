#ejercicio numero 2
print("ejercicio numero 2: ")
print("Velocidad de escape")
print("...................................")
print("Ingrese los valores que se requieren ")
print("...................................")
print("SOLO INGRESAR VALORES NUMERICOS PARA UN CORRECTO FUNCIONAMIENTO")

Pn = float(input("Ingresa el valor de la suscripcion normal: "))
Pp = float(input("Ingresa el valor de la suscripcion Premium: "))
Un = float(input("Ingresa la cantidad de usuarios normales: "))
Up = float(input("Ingresa la cantidad de usuarios Premium: "))
GT = float(input("Ingresa el gasto total: "))

Utilidades = (Pn * Un - GT) + ((Pp + (Pp * 0.5))* Up - GT)

print(f'Las utilidades del proyecto: $ {Utilidades} Dolares')