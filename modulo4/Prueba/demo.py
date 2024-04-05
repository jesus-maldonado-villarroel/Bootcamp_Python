from campaña import Campaña
from anuncio import Video
from datetime import date

v = Campaña("Campaña Demo", date.today(), date.today(), [
    Video("sin-url", "sin-url", "instream", 30)
])

# d = Campaña("Campaña Display", date.today(), date.today(), [
#    Display(250, 100, "url_archivo_display", "url_clic_display", "tradicional")
# ])


# s = Campaña("Campaña Social", date.today(), date.today(), [
#    Social(120, 90, "url_archivo_social", "url_clic_social", "facebook")
# ])

try:
    nombre = input("Ingrese nuevo nombre de la campaña: ")
    sub_tipo = input("Ingrese nuevo subtipo del anuncio: ")

    v.nombre = nombre
    v.anuncios[0].sub_tipo = sub_tipo

except Exception as e:
    with open("modulo4/Prueba/error.log", "a+", encoding="utf-8") as log:
        log.write(f"{e}\n")


print(f"nombre campaña ingresado: {nombre}")
print(f"Subtipo campaña ingresado: {sub_tipo}")
