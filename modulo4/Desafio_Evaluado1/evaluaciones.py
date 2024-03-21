
from pizza import Pizza
from ingredientes import Ingredientes


print("Stock de ingredientes Proteicos: ", Ingredientes.ingredientes_proteico)
print("Stock de ingredientes Vegetales: ", Ingredientes.ingredientes_vegetales)
print("Tipos de Masas disponibles: ", Ingredientes.tipos_masa)


print("Hay salsa de tomate")
print(Pizza.es_valido("salsa de tomate", ["salsa de tomate", "salsa bbq"]))


mipizza = Pizza()
mipizza.realizar_pedido()


print("Ingredientes vegetales:", mipizza.ingredientes_vegetales)
print("Ingrediente proteico:", mipizza.ingrediente_proteico)
print("Tipo de masa:", mipizza.tipo_masa)
print(f"el tamaño de la pizza en general es: {mipizza.tamaño}")
print(f"el precio de la pizza en general es: {mipizza.Precio} pesos")
print("Es una pizza válida:", mipizza.es_valida)


print("Es una clase válida:", Pizza.es_valido(Pizza, [Pizza]))
