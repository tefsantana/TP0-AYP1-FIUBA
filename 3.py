"""
Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos.
Por ejemplo, si recibe los números 1,5,-2,-4, debe devolver 8, que es el producto mas grande
que se puede obtener entre ellos (-2 * -4 = 8).

>>>maximo_producto(1,5,-2,-4)
8
"""

def maximo_producto(num_1, num_2, num_3, num_4):
    '''
    COMPLETAR DOCUMENTACION
    '''
    producto_1_2: int = num_1 * num_2
    producto_1_3: int = num_1 * num_3
    producto_1_4: int = num_1 * num_4
    producto_2_3: int = num_2 * num_3
    producto_2_4: int = num_2 * num_4
    producto_3_4: int = num_3 * num_4

    return max(producto_1_2, producto_1_3, producto_1_4, producto_2_3, producto_2_4, producto_3_4)



