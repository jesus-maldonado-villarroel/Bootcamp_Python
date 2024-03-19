from string import ascii_lowercase
from getpass import getpass


def fuerza_bruta(password):
    intentos = 0
    longitud = len(password)
    for i in range(longitud):
        for letra in ascii_lowercase:
            if password[i] == letra:
                intentos += i + 1
                break
            else:
                intentos += 1
    return intentos


password = getpass("Ingrese la contraseña: ")
intentos = fuerza_bruta(password)
print(f" la contraseña fue forzada en {intentos} intentos.")
