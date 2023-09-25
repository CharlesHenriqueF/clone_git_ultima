import unittest
from unittest.mock import patch
from io import StringIO

def calcular_total_pedido(codigos_pedidos):
    cardapio = {
        100: 9.00,
        101: 11.00,
        102: 12.00,
        103: 12.00,
        104: 14.00,
        105: 17.00,
        200: 5.00,
        201: 4.00
    }

    total = 0.0

    for codigo in codigos_pedidos:
        if codigo in cardapio:
            total += cardapio[codigo]

    return total

class TestRestaurante(unittest.TestCase):

    @patch('builtins.input', side_effect=[100, 101, 999, 102, 2])
    def test_calculo_total_correto(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            total = calcular_total_pedido([100, 101, 999, 102, 2])
            # Agora, verificamos se a mensagem de saída está na saída capturada
            output = mock_output.getvalue()
            self.assertEqual(total, 32.00)
            self.assertIn("O total a ser pago é: 32.00 R$", output)

    @patch('builtins.input', side_effect=[100, 101, 999, 102, 2])
    def test_opcao_invalida(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            total = calcular_total_pedido([100, 101, 999, 102, 2])
            # Agora, verificamos se a mensagem de saída está na saída capturada
            output = mock_output.getvalue()
            self.assertIn("Opção inválida", output)

    @patch('builtins.input', side_effect=[100, 101, 1, 2])
    def test_adicao_itens_correta(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            total = calcular_total_pedido([100, 101, 1, 2])
            # Agora, verificamos se a mensagem de saída está na saída capturada
            output = mock_output.getvalue()
            self.assertEqual(total, 20.00)

    @patch('builtins.input', side_effect=[100, 101, 2])
    def test_calculo_total_apos_adicao(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            total = calcular_total_pedido([100, 101, 2])
            # Agora, verificamos se a mensagem de saída está na saída capturada
            output = mock_output.getvalue()
            self.assertEqual(total, 20.00)
            self.assertIn("O total a ser pago é: 20.00 R$", output)

    @patch('builtins.input', side_effect=[100, 101, 2])
    def test_finalizacao_pedido(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            # Capturamos a saída antes de chamar a função
            output_before = mock_output.getvalue()
            total = calcular_total_pedido([100, 101, 2])
            # Agora, verificamos se a mensagem de saída após a função inclui o total
            output_after = mock_output.getvalue()
            self.assertEqual(total, 20.00)
            self.assertIn("O total a ser pago é: 20.00 R$", output_after)
            # Verificamos se a saída antes da função não inclui o total
            self.assertNotIn("O total a ser pago é:", output_before)

if __name__ == '__main__':
    unittest.main()
