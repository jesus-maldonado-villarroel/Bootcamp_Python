def count_caracteres_diferentes(lorem):
    caracteres_diferentes = set(lorem)
    return len(caracteres_diferentes)


def count_palabras_diferentes(lorem):
    palabras = lorem.split()
    palabras_diferentes = set(palabras)
    return len(palabras_diferentes)


def main():

    with open("lorem_ipsum.txt", "r") as file:
        lorem = file.read()

    caracteres_diferentes = count_caracteres_diferentes(lorem)
    print("Cantidad de caracteres distintos:", caracteres_diferentes)

    palabras_diferentes = count_palabras_diferentes(lorem)
    print("Cantidad de palabras distintas:", palabras_diferentes)


if __name__ == "__main__":
    main()
