"""
Escribir un programa que pida dos números enteros al usuario (a y b) e imprima los primeros a múltiplos de b.

El programa debe validar que cada número que ingrese el usuario sea un entero positivo y, en caso de que no lo sea, solicitarlo nuevamente (hasta que se ingrese algo correcto).

Ejemplo:

>>> Ingrese el número 'a': 4
>>> Ingrese el número 'b': 6
6
12
18
24
Ejemplo con números inválidos:

>>> Ingrese el número 'a': -7
>>> Ingrese el número 'a': hola
>>> Ingrese el número 'a': 3
>>> Ingrese el número 'b': 0
>>> Ingrese el número 'b': 8
8
16
24
"""

def main():
    a = input("Ingrese el número 'a': ")

    while not a.isnumeric() or (int(a) == 0):
        a = input("Ingrese el número 'a': ")

    b = input("Ingrese el número 'b': ")

    while not b.isnumeric() or (int(b) == 0):
        b = input("Ingrese el número 'b': ")

    for numero in range(1, int(a) + 1):

        print(int(b) * numero)

main()

