"""
Se dice que dos números A y B se llaman números amigos si la suma de los divisores de A es igual B y la suma de los divisores de B es igual a A.

NOTA: No se debe tener en cuenta al número como su propio divisor.

##Ejemplo

A = 220
B = 284
Los divisores de A son:
DivA: {1,2,4,5,10,11,20,22,44,55,110}
Si los sumamos obtenemos como resultado 284

Los divisores de B son:
DivB: {1,2,4,71,142}
Si los sumamos obtenemos como resultado 220

Por lo tanto 220 y 284 son números amigos.
"""


def numeros_amigos(a: int, b: int) -> bool:
    '''
    Determina si los números a y b son amigos
    '''
    suma_divisores_a: int = 0
    suma_divisores_b: int = 0

    for posible_divisor_a in range(1, a):

        if (a % posible_divisor_a == 0):
            suma_divisores_a += posible_divisor_a
    
    
    for posible_divisor_b in range(1, b):

        if (b % posible_divisor_b == 0):
            suma_divisores_b += posible_divisor_b
    
    if (suma_divisores_a == b) or (suma_divisores_b == a):
        return True