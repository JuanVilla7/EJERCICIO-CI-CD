import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase):
    
    def test_sumar_numeros_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_sumar_numeros_negativos(self):
        self.assertEqual(sumar(-1, -1), -2)

    def test_sumar_cero(self):
        self.assertEqual(sumar(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
