import pandas as pd

# Variável para parar ou continuar a cadastrar novos produtos
continuar = 0

# Loop para adicionar novos produto
while continuar == 0:

    # Dicionário inicial para armazenar dados dos produtos
    dados_produtos = {'Nome':[],'Descrição':[],'Valor':[],'Disponível':[]}

    # Adicionar os novos produtos
    for item in dados_produtos:
        if item == 'Nome' or item == 'Descrição':
            novo_produto = str(input(f'Qual o(a) {item} do produto?'))

        elif item == 'Disponível':
            novo_produto = str(input(f'O produto está disponível para venda?[sim ou não]: ')).lower()
            while novo_produto not in ['sim', 'nao']:
                novo_produto = str(input(f'Digite um valor válido [sim ou nao]: ')).lower()

        else:
            novo_produto = float(input(f'Qual o(a) {item} do produto? '))

        dados_produtos[item].append(novo_produto)

    # Converte os dados em dataframe    
    df = pd.DataFrame(dados_produtos)

    # Adiciona os novos valores no arquivo de produtos
    df.to_csv('produtos.csv', mode='a', index=False, header=False)

    print("Dados novos adicionados")

    # Carrega os dados do arquivo de produtos
    mostra_produtos = pd.read_csv('produtos.csv')

    # Ordena os produtos pelo Valor
    mostra_produtos_ordenados = mostra_produtos.sort_values(by='Valor')

    # Imprime apenas o nome do produto e o valor
    print(mostra_produtos_ordenados[['Nome', 'Valor']])

    # Input para saber se u usuário desaja adicionar ou não novo produto
    continuar = int(input(f'Deseja cadastrar um novo produto? [0 = sim/1 = não]: '))