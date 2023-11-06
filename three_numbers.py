"""
Problema: Tres Números

Descripción: Escriba un programa que lee tres numeros enteros separados por un espacio y los imprima en una linea
separados por un espacio en forma ordenada de menor a mayor.

Entrada: La entrada consiste de tres números enteros separados por un espacio.
Salida: La salida consiste de los números impresos de menor a mayor.
"""

def three_numbers(input_str: str):
    """Funcion que dada una entrada tipo string con numeros desordenado los ordenas en una nueva cadena ordenada acendente.

    :param input_str: Entrada tipo string de numeros desordenados.
    :return: nueva cadena ordenada de manera acendente.
    """
    #Control de flujo para validar si la funcion cumple las condiciones de ejecucion.
    if type(input_str) == str:
        # Scrip de la funcion.

        # Dividir la cadena en una lista de numeros enteros
        numeros = [int(numero) for numero in input_str.split()]

        # Ordenar la lista de numero de forma acendente
        numeros_ordenados = sorted(numeros)

        # Convertir la lista de numeros en cadena de numeros ordenados separados por espacios.
        resultado = ' '.join(map(str, numeros_ordenados))

        return resultado

    else:
        return "No ingreso numeros enteros separados por espacios en una cadena de texto."

result = three_numbers('5 10 4 12 3 8 2 6 1 2 0 7 6 1 0 8')
print(result)