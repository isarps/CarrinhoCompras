from decor import Item
from servico import Item
from datetime import datetime
import unicodedata

nome: str
data: str
convidados: int
opcao: int
carrinho = []


def normalizar(string: str):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8').lower()


def decoracao_menu():
    decoracao = {
        '1': Item('Arco de balões', 180.00),
        '2': Item('Bolo fake', 50.00),
        '3': Item('Kit de móveis provençais', 180.00),
        '4': Item('Painel de balões', 130.00),
        '5': Item('Painel de tecido', 100.00),
    }


    escolha: str = ''

    while escolha != 'voltar':
        for numero, item in decoracao.items():
            print(f"{numero} - {item.nome}")

        escolha = normalizar(input("\nDigite os itens que deseja adicionar ao carrinho ou voltar: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'voltar':
            for e in getEscolhas:
                if e not in decoracao:
                    print('\nProduto não encontrado.\n')
                    continue
                else:
                    item_escolhido = decoracao[e]
                    carrinho.append(item_escolhido)
                    print(f'Item: {item_escolhido.nome} adicionado ao carrinho.')


def servico_menu():
    servico = {
        '1': Item('Cozinheiro', 170.00),
        '2': Item('Copeiro', 130.00),
        '3': Item('Churrasqueiro', 190.00),
        '4': Item('Recreador', 170.00),
        '5': Item('Recepcionista', 100.00),

    }
    escolha: str = ''

    while escolha != 'voltar':
        for numero, item in servico.items():
            print(f"{numero} - {item.nome}")

        escolha = normalizar(input("\nDigite os itens que deseja adicionar ao carrinho ou voltar: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'voltar':
            for e in getEscolhas:
                if e not in servico:
                    print('\nProduto não encontrado\n.')
                    continue
                else:
                    item_escolhido = servico[e]
                    carrinho.append(item_escolhido)
                    print(f'Item: {item_escolhido.nome} adicionado ao carrinho.')


def local_menu():
    local = {
        '1': Item('Salão', 800.00),
        '2': Item('Chacára', 1000.00),

    }
    escolha: str = ''

    while escolha != 'voltar':
        for numero, item in local.items():
            print(f"{numero} - {item.nome}")

        escolha = normalizar(input("\nDigite os itens que deseja adicionar ao carrinho ou voltar: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'voltar':
            for e in getEscolhas:
                if e not in local:
                    print('\nProduto não encontrado\n.')
                    continue
                else:
                    item_escolhido = local[e]
                    carrinho.append(item_escolhido)
                    print(f'Item: {item_escolhido.nome} adicionado ao carrinho.')


def buffet_menu():
    buffet = {
        '1': Item('Arroz e guarnição', 300.00),
        '2': Item('Bolo de corte', 100.00),
        '3': Item('Churrasco', 400.00),
        '4': Item('Massas', 300.00),
        '5': Item('Bebidas', 500.00),

    }
    escolha: str = ''

    while escolha != 'voltar':
        for numero, item in buffet.items():
            print(f"{numero} - {item.nome}")

        escolha = normalizar(input("\nDigite os itens que deseja adicionar ao carrinho ou voltar: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'voltar':
            for e in getEscolhas:
                if e not in buffet:
                    print('\nProduto não encontrado\n.')
                    continue
                else:
                    item_escolhido = buffet[e]
                    carrinho.append(item_escolhido)
                    print(f'Item: {item_escolhido.nome} adicionado ao carrinho.')


def menu():
    print("\n|---------------|")
    print("|  1-Buffet     |\n|  2-Decoração  | \n|  3-Local      | \n|  4-Serviços   | \n|  0-Finalizar  |")
    print("|---------------|")
    return int(input("\nDigite qual opção deseja selecionar primeiro: "))


def exibir_carrinho():
    total: float = 0
    print(f"{nome}, estes são os dados do seu evento:")
    print(f"Cidade: {cidade} \nQuantidade de convidados: {convidados} \nData do evento{data}:")
    print("|-------------------------------------------------|")
    for item_selecionado in carrinho:
        total += item_selecionado.preco
        print(f"|--\t{item_selecionado.nome} R$ {item_selecionado.preco:.2f}")
    print(f"|\tTotal = R$ {total:.2f}")


print("Bem-vindo ao iFest!")

nome = input("\nOlá, qual seu nome? ").capitalize()
convidados = int(input(f"{nome}, a festa é para quantos convidados? "))
data = input("Em qual data pretende realizar o evento? ")
cidade = input("Qual cidade você prefere realizar o evento? ").capitalize()


while True:
    opcao = menu()
    match opcao:
        case 1:
            buffet_menu()
        case 2:
            decoracao_menu()
        case 3:
            local_menu()
        case 4:
            servico_menu()
        case 0:
            break
    exibir_carrinho()

exibir_carrinho()
