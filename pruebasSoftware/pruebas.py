import doctest

## prueba de modulo
def cuadrados(lista):
    """
    Funcion que hace el cuadrado de los elementos de una lista.
    :param lista: lista de numeros
    :return: lista de cuadrados

    >>> lista = [1,2,3,4]
    >>> cuadrados(lista)
    [1, 4, 9, 16]
    """
    return [n ** 2 for n in lista]

def cuadrado(numero):
    """
    Funcion que crea el cuadrado de un unico numero de la lista.
    :param numero: numero
    :return: numero**2

    >>> l = [0, 2, 5, 100]
    >>> for n in l:
    ...     cuadrado(n)
    0
    4
    25
    10000
    """

    return numero**2




def _test():
    doctest.testmod()

if __name__ == "__main__":
    _test()