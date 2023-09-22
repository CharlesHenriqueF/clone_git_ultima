# Definindo o decorator
def decorator_imprimir(funcao):
    def wrapper(capital, taxa_de_juro, tempo_de_emprestimo):
        
        print(f"Capital: {capital}")
        print(f"Taxa de Juro: {taxa_de_juro}")
        print(f"Tempo de Empréstimo: {tempo_de_emprestimo}")
        
        resultado = funcao(capital, taxa_de_juro, tempo_de_emprestimo)
        
        # Imprimir o resultado
        print(f"Resultado: {resultado}")
        
        return resultado
    return wrapper

# Exemplo de função que calcula juros
@decorator_imprimir
def calcular_juros_simples(capital, taxa_de_juro, tempo_de_emprestimo):
    juros = (capital * taxa_de_juro * tempo_de_emprestimo) / 100
    montante = capital + juros
    return montante

calcular_juros_simples(1000, 5, 2)
