from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse(
        """
    <h1>Este es el titulo de la aplicacion web</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt est quisquam adipisci rem quae dolorum numquam consequatur tempore ipsam magni, ab voluptas consequuntur exercitationem? Quo, in. Ullam enim beatae ea!</p>
    """
    )


def about(request):
    return HttpResponse(
        """
    <h2>informacion sobre la empresa</h2>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt est quisquam adipisci rem quae dolorum numquam consequatur tempore ipsam magni, ab voluptas consequuntur exercitationem? Quo, in. Ullam enim beatae ea!</p>
    """
    )


def contacto(request):
    return HttpResponse(
        """
    <html lang="es">
    <head>
	<meta charset="UTF-8">
	<title>Formulario de contacto</title>


  
    </head>


<body>	
  
  <!-- formulario de contacto en html y css -->  

	<div class="contact_form">

		<div class="formulario">			
      <h1>Formulario de contacto</h1>
				<h3>Escríbenos y en breve los pondremos en contacto contigo</h3>


					<form action="submeter-formulario.php" method="post">				

						
								<p>
									<label for="nombre" class="colocar_nombre">Nombre
										<span class="obligatorio">*</span>
									</label>
										<input type="text" name="introducir_nombre" id="nombre" required="obligatorio" placeholder="Escribe tu nombre">
								</p>
							
								<p>
									<label for="email" class="colocar_email">Email
										<span class="obligatorio">*</span>
									</label>
										<input type="email" name="introducir_email" id="email" required="obligatorio" placeholder="Escribe tu Email">
								</p>
						
								<p>
									<label for="telefone" class="colocar_telefono">Teléfono
									</label>
										<input type="tel" name="introducir_telefono" id="telefono" placeholder="Escribe tu teléfono">
								</p>		
									
							
								<p>
									<label for="asunto" class="colocar_asunto">Asunto
										<span class="obligatorio">*</span>
									</label>
										<input type="text" name="introducir_asunto" id="assunto" required="obligatorio" placeholder="Escribe un asunto">
								</p>		
							
								<p>
									<label for="mensaje" class="colocar_mensaje">Mensaje
										<span class="obligatorio">*</span>
									</label>                     
                               		  <textarea name="introducir_mensaje" class="texto_mensaje" id="mensaje" required="obligatorio" placeholder="Deja aquí tu comentario..."></textarea> 
                               	</p>	  								
							
								<button type="submit" name="enviar_formulario" id="enviar"><p>Enviar</p></button>

								<p class="aviso">
									<span class="obligatorio"> * </span>los campos son obligatorios.
								</p>					
						
					</form>
		</div>	
	</div>

</body>
</html>

    """
    )
