def ingreso_numero(mensaje):
    while True:
        num = int(input(mensaje))
        if num > 0:
            break
    return num 


# Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1.
def calcular_factorial(numero):
    factorial = 1
    i = 1
    while True:
        factorial *= i # factorial = fatorial * i
        i += 1
        if i > numero:
            break
    return factorial    

numero = ingreso_numero('Ingrese numero 1')
# numero_2 = ingreso_numero('Ingrese numero 2')
factorial = calcular_factorial(numero)
print(f'Fatorial del {numero} es: {factorial}')  