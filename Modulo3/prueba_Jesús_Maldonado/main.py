from template_api import lista_img
from string import Template

image_card = """<div class="card" style="width: 18rem;">
                <img src="$url" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">$title</h5>
                    <p class="card-text">$title2</p>
                </div>
            </div>
    """

img_template = Template(image_card)
texto_img = ''

for img, title, title2 in lista_img:
    texto_img += img_template.substitute(url=img,
                                         title=title, title2=title2) + '\n'


html_template = Template('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Amantes pajaros Chile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1 class="text-center">Aves Nativas de Chile</h1>
    <div class="container">
        <div class="row">
            $body
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body=texto_img)

archivo = open('prueba_Jesús_Maldonado\index.html',
               'w+', encoding='utf-8')
archivo.write(html)
archivo.close()
