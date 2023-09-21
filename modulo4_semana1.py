import requests
import json  # Importe a biblioteca json

class FipeCarIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = []
        self.index = 0

    def fetch_modelos(self):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos'
        headers = {'user-agent': 'MyStudyApp'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            self.modelos = data['modelos']

    def __iter__(self):
        self.fetch_modelos()
        return self

    def __next__(self):
        if self.index < len(self.modelos):
            modelo = self.modelos[self.index]
            self.index += 1
            return modelo
        else:
            raise StopIteration

def listar_marcas():
    url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
    headers = {'user-agent': 'MyStudyApp'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("Marcas Disponíveis:")
        for marca in data:
            print(f"{marca['id']} - {marca['nome']}")

def main():
    listar_marcas()
    marca_id = input("Digite o ID da marca desejada: ")

    try:
        marca_id = int(marca_id)
        car_iterator = FipeCarIterator(marca_id)
        
        print("\nModelos de carros da marca selecionada:")
        for modelo in car_iterator:
            print(f"Nome: {modelo['nome']}, ID: {modelo['codigo']}")

    except ValueError:
        print("ID da marca deve ser um número inteiro válido.")

if __name__ == "__main__":
    main()
