# usando while True

print("PASO A PASO DE PRIMEROS AUXILIOS")
print("#################################")

print("MENU: SOLO RESPONDER \n si\n no")


def primeros_aux(preguntas):
    ambulancia_llego = False
    while not ambulancia_llego:
        if preguntas == "si":
            print("Valorar la necesidad de llevarlo al hospital mas cercano")
            ambulancia_llego = True
        elif preguntas == "no":
            print("Abrir la via aerea\n")
            respuesta = input("Respira? (1-si, 2-no): ")
            if respuesta == "si":
                print("Permitirle posicion de suficiente ventilacion \n")
                ambulancia_llego = True
            elif respuesta == "no":
                print("Administrar 5 ventilaciones y llamar a la ambulancia \n")
                respuesta = input("Signos de vida? (1-si, 2-no): ")
                if respuesta == "si":
                    print("Reevaluar a la espera de la ambulancia\n")
                    ambulancia_llego = False
                elif respuesta == "no":
                    print(
                        "Administrar Compresiones toracicas hasta que llegue la ambulancia \n")
                    respuesta = input("Llego la ambulancia? (1-si, 2-no): ")
                    if respuesta == "si":
                        print("su paciente se salvara \n")
                        ambulancia_llego = True
                    elif respuesta == "no":
                        while not ambulancia_llego:
                            respuesta = input("Signos de vida? (1-si, 2-no): ")
                            if respuesta == "si":
                                print("Reevaluar a la espera de la ambulancia\n")
                                ambulancia_llego = False
                            elif respuesta == "no":
                                print(
                                    "Administrar Compresiones toracicas hasta que llegue la ambulancia \n")
                                respuesta = input(
                                    "Llego la ambulancia? (1-si, 2-no): ")
                                if respuesta == "si":
                                    print("su paciente se salvara \n")
                                    ambulancia_llego = True
                                elif respuesta == "no":
                                    ambulancia_llego = False


preguntas = input("¿Responde a estimulos? (si/no): ")
primeros_aux(preguntas)
