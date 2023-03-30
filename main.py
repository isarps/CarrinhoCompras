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
        'arco de baloes': Item('Arco de balões', 180.00),
        'bolo fake': Item('Bolo fake', 50.00),
        'kit de moveis provençais': Item('Kit de móveis provençais', 180.00),
        'painel de baloes': Item('Painel de balões', 130.00),
        'painel de tecido': Item('Painel de tecido', 100.00),
    }

    escolha: str = ''

    while escolha != 'fim':
        for item in decoracao.values():
            print(item.nome)

        escolha = normalizar(input("Digite os itens que deseja adicionar ao carrinho ou fim: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'fim':
            for e in getEscolhas:
                if e not in decoracao:
                    print('Produto não encontrado.')
                    continue
                else:
                    item_escolhido = decoracao[e]
                    carrinho.append(item_escolhido)
                    print(f'{item_escolhido.nome} adicionado ao carrinho.')


def servico_menu():
    servico = {
        'cozinheiro': Item('Cozinheiro', 170.00),
        'copeiro': Item('Copereiro', 130.00),
        'churrasqueiro': Item('Churrasqueiro', 190.00),
        'recreador': Item('Recreador', 170.00),
        'recepcionista':Item('Recepcionista', 100.00)
    }
    escolha: str = ''

    while escolha != 'fim':
        for item in servico.values():
            print(item.nome)

        escolha = normalizar(input("Digite os itens que deseja adicionar ao carrinho ou fim: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'fim':
            for e in getEscolhas:
                if e not in servico:
                    print('Produto não encontrado.')
                    continue
                else:
                    item_escolhido = servico[e]
                    carrinho.append(item_escolhido)
                    print(f'{item_escolhido.nome} adicionado ao carrinho.')


def local_menu():
    local = {
        'Salão': Item('Salão', 800.00),
        'chacara': Item('Chacára', 1000.00),
    }
    escolha: str = ''

    while escolha != 'fim':
        for item in local.values():
            print(item.nome)

        escolha = normalizar(input("Digite os itens que deseja adicionar ao carrinho ou fim: "))

        getEscolhas = escolha.split(", ")

        # Verificar se o produto existe no dicionário de produtos
        if escolha != 'fim':
            for e in getEscolhas:
                if e not in local:
                    print('Produto não encontrado.')
                    continue
                else:
                    item_escolhido = local[e]
                    carrinho.append(item_escolhido)
                    print(f'{item_escolhido.nome} adicionado ao carrinho.')


def buffet_menu():
    buffet = {
        'arroz e guarnicao': Item('Arroz e guarnição', 300.00),
        'bolo de corte': Item('Bolo de corte', 100.00),
        'churrasco': Item('Churrasco', 400.00),
        'massas': Item('Massas', 300.00),
        'bebidas': Item('Bebidas', 500.00),
    }
    escolha: str = ''

    while escolha != 'fim':
        for item in buffet.values():
            print(item.nome)

        escolha = normalizar(input("Digite os itens que deseja adicionar ao carrinho ou fim: "))

        # Verificar se o produto existe no dicionário de produtos
        if escolha not in buffet:
            if escolha != 'fim':
                print('Produto não encontrado.')
            continue

        item_escolhido = buffet[escolha]
        # Adicionar o produto ao carrinho
        carrinho.append(item_escolhido)
        # Adicionar o preço do produto ao total da compra
        print(f'{item_escolhido.nome} adicionado ao carrinho.')


def menu():
    print("\n1-Buffet \n2-Decoração \n3-Local \n4-Serviços \n0-Finalizar")
    return int(input("Digite qual opção deseja selecionar primeiro: "))


def exibir_carrinho():
    total: float = 0
    print("|-------------------------------------------------|")
    print("|--------------Itens adicionados------------------|")
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
