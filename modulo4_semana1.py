import requests
import json

class FipeCarIterator:
    def __init__(self, id_marca):
        self.id_marca = id_marca
        self.indice = 0
        self.modelos = []

    def obter_modelos(self):
        headers = {'user-agent': 'MyStudyApp'}
        resposta = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.id_marca}/modelos', headers=headers)

        if resposta.status_code == 200:
            dados = json.loads(resposta.text)
            self.modelos = dados['modelos']
        else:
            print(f'Erro ao acessar a API: {resposta.status_code}')

    def __iter__(self):
        self.obter_modelos()  # Move a obtenção de modelos para __iter__
        return self

    def __next__(self):
        if self.indice < len(self.modelos):
            modelo = self.modelos[self.indice]
            self.indice += 1
            return (modelo['nome'], modelo['codigo'])
        else:
            raise StopIteration

def listar_marcas():
    headers = {'user-agent': 'MyStudyApp'}
    resposta = requests.get('https://parallelum.com.br/fipe/api/v1/carros/marcas', headers=headers)

    if resposta.status_code == 200:
        marcas = json.loads(resposta.text)
        print('Marcas disponíveis na API:')
        for marca in marcas:
            print(f'{marca["nome"]} - {marca["codigo"]}')
    else:
        print(f'Erro ao acessar a API: {resposta.status_code}')

def main():
    listar_marcas()
    id_marca = input('Digite o ID da marca que você deseja consultar: ')
    iterator = FipeCarIterator(id_marca)
    print('Modelos de carros encontrados:')
    for nome, codigo in iterator:
        print(f'{nome} - {codigo}')

if __name__ == "__main__":
    main()
