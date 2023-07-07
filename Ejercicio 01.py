5def realizar_operacion(operador, num1, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        return None

def calcular(cadena):
    operadores_prioridad = {"+": 1, "-": 1, "*": 2, "/": 2}

    partes = cadena.split()
    numeros = [float(num) for num in partes[::2]]
    operadores = partes[1::2]

    while len(operadores) > 0:
        index = 0
        max_prioridad = 0

        for i, operador in enumerate(operadores):
            if operadores_prioridad[operador] > max_prioridad:
                max_prioridad = operadores_prioridad[operador]
                index = i

        operador = operadores.pop(index)
        num1 = numeros[index]
        num2 = numeros[index + 1]
        resultado = realizar_operacion(operador, num1, num2)

        numeros[index] = resultado
        del numeros[index + 1]

    return numeros[0]

# Ejemplo de uso
cadena = input("Ingrese la operación en formato 'num1 operador num2 operador ...': ")

# Validar la cantidad de números en la cadena
numeros = cadena.split()
if len(numeros) <= 20:
    resultado = calcular(cadena)
    if resultado is not None:
        print("El resultado es:", resultado)
else:
    print("¡Error! La cantidad de números debe ser menor a 20.")
