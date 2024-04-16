--1.Crear una base de datos llamada películas.
--CREATE DATABASE peliculas;

--2. Cargar ambos archivos a su tabla correspondiente. SE CARGARON LOS ARCHIVOS. csv

--CREATE TABLE public.peliculas (
--	id int4 NULL,
--	"Pelicula" varchar(64) NULL,
--	"Año estreno" int4 NULL,
--	"Director" varchar(50) NULL
--);

--CREATE TABLE public.reparto (
--	id_pelicula int4 NULL,
--	actor varchar(50) NULL
--);

--SELECT * FROM peliculas;
--SELECT * FROM reparto;

--3. Obtener el ID de la película “Titanic”.
--SELECT id as ID_Pelicula_Titanic from peliculas where "Pelicula" = 'Titanic';

--4. Listar a todos los actores que aparecen en la película "Titanic".
--SELECT actor as Actores_que_aparecen_en_titanic from reparto where id_pelicula = 2;

--5.Consultar en cuántas películas del top 100 participa Harrison Ford.
--SELECT * FROM reparto WHERE actor = 'Harrison Ford';

--6.Indicar las películas estrenadas entre los años 1990 y 1999 ordenadas por título demanera ascendente.
--SELECT * FROM peliculas WHERE "Año estreno" >= 1990 and "Año estreno" <= 1999 ORDER BY "Pelicula" ASC;

--7. Hacer una consulta SQL que muestre los títulos con su longitud, la longitud debe ser nombrado para la consulta como “longitud_titulo”.
--SELECT "Pelicula", LENGTH("Pelicula") as logitud_titulo from peliculas;

--8. Consultar cual es la longitud más grande entre todos los títulos de las películas.
--SELECT MAX(LENGTH("Pelicula")) as Pelicula_con_mayor_longitud_de_nombre FROM peliculas;