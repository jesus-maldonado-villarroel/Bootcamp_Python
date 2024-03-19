
def validate(opciones, eleccion):
    # Definir validación de eleccion
    ##########################################################################
    if eleccion not in opciones:
        print("opciones no valida")
        nueva_eleccion = input("Ingrese una nueva opcion: ")
        return validate(opciones, nueva_eleccion)
    ##########################################################################
    return eleccion


if __name__ == '__main__':

    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0', '1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(numeros, eleccion)
