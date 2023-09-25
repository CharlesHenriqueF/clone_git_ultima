import unittest
from io import StringIO
from unittest.mock import patch


# Inclua os testes aqui

class TestFreteCalculator(unittest.TestCase):

    @patch('builtins.input', side_effect=["20", "30", "40"])
    def test_calculo_preco_volume(self, mock_input):
        from your_code_file import calcular_preco_volume
        preco = calcular_preco_volume(20 * 30 * 40)
        self.assertEqual(preco, 30.0)

    @patch('builtins.input', side_effect=["20", "30", "40"])
    def test_calculo_multiplicador_peso(self, mock_input):
        from your_code_file import calcular_multiplicador_peso
        multiplicador = calcular_multiplicador_peso(20)
        self.assertEqual(multiplicador, 1.0)

    @patch('builtins.input', side_effect=["BR"])
    def test_calculo_multiplicador_rota(self, mock_input):
        from your_code_file import calcular_multiplicador_rota
        multiplicador = calcular_multiplicador_rota("BR")
        self.assertEqual(multiplicador, 1.5)

    @patch('builtins.input', side_effect=["20", "30", "40", "20", "BR"])
    def test_calculo_frete_total(self, mock_input):
        from your_code_file import calcular_frete
        total = calcular_frete(20 * 30 * 40, 1.0, 1.5)
        self.assertEqual(total, 1800.0)

    @patch('builtins.input', side_effect=["Texto", "20", "30", "40"])
    def test_entrada_nao_numerica(self, mock_input):
        from your_code_file import validar_medida
        medida = validar_medida("Texto")
        self.assertEqual(medida, -1)

if __name__ == '__main__':
    unittest.main()
