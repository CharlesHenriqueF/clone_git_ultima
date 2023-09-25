import unittest
from io import StringIO
from unittest.mock import patch
import sys
print(sys.path)
# Importe as funções e variáveis do seu código aqui
from atividade_m3s3_codigo4 import gerar_codigo, cadastrar_peca, consultar_pecas, remover_peca

class TestSistemaGerenciamentoPecas(unittest.TestCase):

    @patch('builtins.input', side_effect=["20", "30", "40"])
    def test_gerar_codigo(self, mock_input):
        # Teste se a função gera códigos únicos para cada peça cadastrada
        # Crie algumas peças manualmente e verifique se os códigos são únicos
        # Exemplo:
        sys.stdin = StringIO("20\n30\n40\n")
        pecas.clear()
        self.assertEqual(gerar_codigo(), 1)

    @patch('builtins.input', side_effect=["Nome da Peça", "Fabricante", "50.0"])
    def test_cadastrar_peca(self, mock_input):
        # Teste se a função cadastra uma peça corretamente na lista de peças
        # Adicione uma peça usando a função cadastrar_peca
        # Verifique se a peça foi adicionada corretamente à lista de peças
        # Exemplo:
        sys.stdin = StringIO("Nome da Peça\nFabricante\n50.0\n")
        pecas.clear()
        cadastrar_peca()
        self.assertEqual(len(pecas), 1)

    @patch('builtins.input', side_effect=["BR"])
    def test_consultar_pecas(self, mock_input):
        # Teste se a função consultar_pecas retorna informações corretas
        # Crie algumas peças manualmente e verifique se a função retorna informações corretas
        # Teste também a consulta por código e fabricante
        # Exemplo:
        sys.stdin = StringIO("BR\n")
        pecas.clear()
        cadastrar_peca()
        sys.stdout = StringIO()
        consultar_pecas()
        output = sys.stdout.getvalue()
        self.assertIn("Nome da Peça", output)
        self.assertIn("Fabricante", output)
        self.assertIn("50.00 R$", output)

    @patch('builtins.input', side_effect=["20", "30", "40"])
    def test_remover_peca(self, mock_input):
        # Teste se a função remover_peca remove uma peça corretamente
        # Adicione uma peça usando cadastrar_peca e, em seguida, remova-a usando a função
        # Verifique se a peça foi removida da lista de peças
        # Exemplo:
        sys.stdin = StringIO("20\n30\n40\n")
        pecas.clear()
        cadastrar_peca()
        remover_peca()
        self.assertEqual(len(pecas), 0)

if __name__ == '__main__':
    unittest.main()
