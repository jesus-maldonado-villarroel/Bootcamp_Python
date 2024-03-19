from random import choice


def jugar_piedra_papel_tijera(jugador, maquina):
    opciones = ["piedra", "papel", "tijera"]

    if jugador == maquina:
        return "Empate"

    elif jugador == "piedra":
        if maquina == "papel":
            return "Maquina gana"
        else:
            return "Jugador gana"

    elif jugador == "papel":
        if maquina == "tijera":
            return "Maquina gana"
        else:
            return "Jugador gana"

    elif jugador == "tijera":
        if maquina == "piedra":
            return "Maquina gana"
        else:
            return "Jugador gana"


def main():
    opciones = ["piedra", "papel", "tijera"]
    print("Jan ken gēmu e yōkoso!\n")
    jugador = input("Elige: piedra, papel o tijera: ").lower()
    maquina = choice(["piedra", "papel", "tijera"])
    if jugador not in opciones:
        print("Argumento invalido: Debe ser piedra, papel o tijera")
        return main()
    resultado = jugar_piedra_papel_tijera(jugador, maquina)
    print(f"Jugador elige {jugador}")
    print(f"Maquina elige {maquina}")
    print(resultado)


if __name__ == '__main__':
    main()
