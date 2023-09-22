import unittest
from io import StringIO
import sys

from atividade_m3s2 import calcular_juros_simples

class TesteCalculoJurosSimples(unittest.TestCase):
    def setUp(self):
        self.old_stdout = sys.stdout
        sys.stdout = StringIO()
    
    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_calculo_juros_simples(self):
        resultado = calcular_juros_simples(1000, 5, 2)
        
        output = sys.stdout.getvalue()

        # Verificar se o resultado é igual a 1100.0 (1000 + 5% de juros em 2 anos)
        self.assertEqual(resultado, 1100.0)

        # Verificar se a saída contém as variáveis e o resultado
        self.assertIn("Capital: 1000", output)
        self.assertIn("Taxa de Juro: 5", output)
        self.assertIn("Tempo de Empréstimo: 2", output)
        self.assertIn("Resultado: 1100.0", output)

if __name__ == '__main__':
    unittest.main()
