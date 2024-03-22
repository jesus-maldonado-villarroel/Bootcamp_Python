from personaje import Personaje
import random

print("Bienvenido a Gran Fantasia")

nombre = input("Por favor indique el nombre de su personaje: \n")

p = Personaje(nombre)

print("Oh no, Ha aparecido un Orco!")

o = Personaje("Orco")

probabilidad_ganar = p.get_probabilidad_ganar(o)

opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)


while opcion_orco == 1:
    numero = random.uniform(0, 1)
    resultado = "Ganaste" if numero < probabilidad_ganar else "Perdiste"
    if resultado == "Ganaste":
        print(f"""Le has ganado al orco, Felicidades!
            Recibiras 50 puntos de experiencia!    
            """)
        p.estado = 50
        o.estado = -30

    elif resultado == "Perdiste":
        print(f"""has Perdido!
            El Orco Recibira 50 puntos de experiencia!
            Tu pierdes 30 puntos de experiencia!    
            """)
        p.estado = -30
        o.estado = 50

    print(p.estado)
    print(o.estado)

    probabilidad_ganar = p.get_probabilidad_ganar(o)
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)


print("has huido, el orco ha quedado atras")
