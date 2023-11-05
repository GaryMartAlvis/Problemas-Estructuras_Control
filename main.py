"""
Problema 1372: Años Bisiesto
Descripción: Los años bisiestos tienen 366 dias y son aquellos que son multiplos de 4 y no terminan con dos ceros o
aquellos que despues de quitar los dos ceros del final son divisibles por 4 (divisibles por 400). Por ejemplo 1800 ,
y 1900 no son años bisiestos, sin embargo el año 2000 si lo fue.

Entrada: La entrada consiste de numeros naturales en el rango de 1800 y 9999. Salida: En la salida escriba una palabra
que diga "si " si fue biciesto y "no " si no fue bisiesto, sin comillas.
"""


def leap_yerar(year):
    ''' Función que dado un año devuelve como resultado si el año es bisiesto o no.

    :param year: Numero dado por el usuario el cual respresenta el año.
    :return: resultado de la identificación del año como bisiesto o no bisiesto.
    '''

    if year % 4 == 0:
        return 'Si'
    return 'No'


result = leap_yerar(2020)
print(leap_yerar.__doc__)
print(result)
