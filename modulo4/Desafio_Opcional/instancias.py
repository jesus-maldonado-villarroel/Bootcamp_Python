from te import Te


te_instancia_1 = Te()
te_instancia_2 = Te()


tipo_instancia_1 = type(te_instancia_1)
tipo_instancia_2 = type(te_instancia_2)


print("Tipo de instancia 1:", tipo_instancia_1)
print("Tipo de instancia 2:", tipo_instancia_2)


if tipo_instancia_1 == tipo_instancia_2:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")
