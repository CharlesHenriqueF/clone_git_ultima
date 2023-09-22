import unittest
import requests
import json
from modulo4_semana1 import FipeCarIterator  # Substitua "modulo4_semana1" pelo nome do seu módulo

class TestDaClasse(unittest.TestCase):

    def test_obter_modelos(self):
        # Crie uma instância do FipeCarIterator com um ID de marca real para testar
        iterator = FipeCarIterator(id_marca=1)

        # Verifique se a lista de modelos não está vazia
        iterator.obter_modelos()
        self.assertTrue(iterator.modelos)

def obter_ids_de_marcas():
    headers = {'user-agent': 'MyStudyApp'}
    resposta = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas', headers=headers)

    if resposta.status_code == 200:
        marcas = json.loads(resposta.text)
        return [marca['codigo'] for marca in marcas]
    else:
        print(f'Erro ao acessar a API: {resposta.status_code}')
        return []

def criar_testes_para_ids_de_marcas():
    ids_de_marcas = obter_ids_de_marcas()
    suite = unittest.TestSuite()

    for id_marca in ids_de_marcas:
        subclass_name = f'TestNomeDaClasseDeTeste_{id_marca}'
        subclass = type(subclass_name, (TestDaClasse,), {})

        tests = unittest.defaultTestLoader.loadTestsFromTestCase(subclass)
        suite.addTests(tests)

    return suite

if __name__ == '__main__':
    suite = criar_testes_para_ids_de_marcas()
    unittest.TextTestRunner().run(suite)
