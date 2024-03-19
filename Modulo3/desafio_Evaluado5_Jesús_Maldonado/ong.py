def calcular(fact_1=5, prod_1=[4, 6, 7, 4, 3], fact_2=6):

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        elif n > 1:
            return n * factorial(n-1)

    def calcular_productoria():
        resultado = 1
        for num in prod_1:
            resultado *= num
        return resultado

    fact_1_resultado = factorial(fact_1)
    prod_1_resultado = calcular_productoria()
    fact_2_resultado = factorial(fact_2)

    return fact_1_resultado, prod_1_resultado, fact_2_resultado


resultado_fact_1, resultado_prod_1, resultado_fact_2 = calcular()

print("El factorial de 5 es ", resultado_fact_1)
print("La productoria de [4, 6, 7, 4, 3] es ", resultado_prod_1)
print("El factorial de 6 es ", resultado_fact_2)
