#ejercicio numero 1
print("ejercicio numero 1: ")
print("Velocidad de escape")
print("...................................")
print("Ingrese los valores que se requieren ")
print("...................................")

from math import sqrt, ceil

g = float(input("Ingresa constante gravitacional: "))
r = float(input("Ingresa el radio del planeta en kilometros: "))

ve = sqrt(2*g*(r*1000))

print(f'La velocidad de escape es de: {round(ve,1)} [m/2]')









