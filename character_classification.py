"""
Problema: Clasificación de Caracteres

Descripción: Escriba un programa que lea una letra, y diga si esta letra es minúscula, mayúscula.
También debe indicar si es una vocal o consonante.
Para leer un caracter del teclado se utiliza la siguiente instrucción:
char c = (char) System.in.read();
En Python ouede leerlo con:
c = input()
Ejemplo de entrada 1
a
Ejemplo de salida 1
minuscula
vocal
Ejemplo de entrada 2
Ejemplo de salida 2
mayuscula
consonante

Entrada:La entrada consiste de una letra.
Salida: En la salida escriba si es una letra minúscula o mayúscula. En  otra linea escriba si es vocal o consonante.
"""


def character_classification(letter):
    """ Función para clasificación de caracteres
    :param letter:
    :return: Clasificación de la letra
    """

    if letter.isalpha():
        # Clasifica entre vocal y consonante
        if letter.lower() in 'aeiou':
            print("Vocal")
        else:
            print("Consonante")

        # Clasifica entre Mayúscula y Minúscula
        if letter.isupper():
            print("Mayúscula")
        else:
            print("Minúscula")
    else:
        print("El caracter ingresado no es una letra")


letter = input("Ingresa un caracter para clasificarlo: ")
character_classification(letter)