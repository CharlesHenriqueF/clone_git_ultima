import unittest
from unittest.mock import patch
from io import StringIO

def calcular_valor_total(valor_unitario, quantidade):
    desconto = 1

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade

    return valor_sem_desconto, valor_com_desconto

class TestCalculoValorTotal(unittest.TestCase):

    def test_calculo_valor_total_com_desconto_10_99(self):
        valor_sem_desconto, valor_com_desconto = calcular_valor_total(10, 50)
        self.assertEqual(valor_sem_desconto, 500)
        self.assertEqual(valor_com_desconto, 475)

    def test_calculo_valor_total_com_desconto_100_999(self):
        valor_sem_desconto, valor_com_desconto = calcular_valor_total(20, 500)
        self.assertEqual(valor_sem_desconto, 10000)
        self.assertEqual(valor_com_desconto, 9000)

    def test_calculo_valor_total_com_desconto_1000(self):
        valor_sem_desconto, valor_com_desconto = calcular_valor_total(30, 1000)
        self.assertEqual(valor_sem_desconto, 30000)
        self.assertEqual(valor_com_desconto, 25500)

    def test_calculo_valor_total_sem_desconto(self):
        valor_sem_desconto, valor_com_desconto = calcular_valor_total(40, 5)
        self.assertEqual(valor_sem_desconto, 200)
        self.assertEqual(valor_com_desconto, 200)

if __name__ == '__main__':
    unittest.main()
