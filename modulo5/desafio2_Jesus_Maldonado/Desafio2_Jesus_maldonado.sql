--desafio2 terminado Jesus_MALDONADO 

--select * from inscritos;
--select COUNT(*) as Total_de_registros FROM inscritos;
--select SUM(cantidad) as TOTAL_inscritos from inscritos;
--select * from inscritos where fecha in (select MIN(fecha) from inscritos);
--select SUM(cantidad) as incritos_por_dia, fecha from inscritos GROUP BY fecha;
--select SUM(cantidad) as Total_inscritos, fecha as Dia_de_mayor_Inscritos from inscritos GROUP BY fecha ORDER BY Dia_de_mayor_Inscritos DESC limit 1;