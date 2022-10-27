import unittest
from unittest import result
from ejercicio_1.calculadora import dividir, elevar, restar, suma

class TestCalculadora(unittest.TestCase):
    def test_sumarNumeros(self):
        result = suma(3, 5)
        self.assertEqual(result, 8)

    def test_resta(self):
        result = restar(5, 3)
        self.assertEqual(result, 2)
    
    def test_elevar(self):
        result = elevar(8, 2)
        self.assertEqual(result, 64)

    def test_excepcionDividirEntreCero(self):
        with self.assertRaises(ZeroDivisionError):
            result = dividir(3, 0)



if __name__ == '__main__':
    unittest.main()