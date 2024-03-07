import unittest

def cuadrado (numero):
    return numero**2

class EjemploPruebas(unittest.TestCase):
    def test(self):
        lista = [0, 2, 5, 100]
        resultado = [cuadrado(n) for n in lista]
        self.assert(r, [4,25])


        # pass
        # raise AssertionError()

if __name__=="__main__":
    unittest.main()

