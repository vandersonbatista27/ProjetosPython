# Carrinho de compras
# Este programa permite adicionar, exibir, remover itens, calcular o total e sair.

# Inicialize listas vazias para armazenar nomes e preços
nome_dos_itens = []
preco_dos_itens = []


def adicionar_itens():
    nome_do_item = input("Qual item você gostaria de adicionar? ")
    nome_dos_itens.append(nome_do_item)
    preco_do_item = float(input(f"Qual é o preço do(a) '{nome_do_item}'? "))
    preco_dos_itens.append(preco_do_item)
    print(f"'{nome_do_item}' foi adicionado ao carrinho.")


def mostra_carrinho():
    if not nome_dos_itens:
        print("O carrinho de compras está vazio.")
    else:
        print("O que tem no carrinho de compras é:")
        for i, (nome, preco) in enumerate(zip(nome_dos_itens, preco_dos_itens), 1):
            print(f"{i}. {nome} - R${preco:.2f}")


def remover_item():
    if not nome_dos_itens:
        print("O carrinho de compras está vazio. Não há nada para remover.")
        return

    mostra_carrinho()
    numero_do_item = int(input("Qual item você gostaria de remover? "))

    if 1 <= numero_do_item <= len(nome_dos_itens):
        remover_nome = nome_dos_itens.pop(numero_do_item - 1)
        remover_preco = preco_dos_itens.pop(numero_do_item - 1)
        print(f"'{remover_nome}' foi removido do carrinho.")
    else:
        print("Desculpe, esse número não é válido.")


def calculo_total():
    total = sum(preco_dos_itens)
    print(f"O preço total dos itens no carrinho de compras é R${total:.2f}")


while True:
    print("\nOpções do menu:")
    print("1. Adicionar um novo item")
    print("2. Ver carrinho de compras")
    print("3. Remover um item")
    print("4. Calcule o total")
    print("5. Sair")

    escolha = input("Digite um destes números (1/2/3/4/5): ")

    if escolha == '1':
        adicionar_itens()
    elif escolha == '2':
        mostra_carrinho()
        calculo_total()
    elif escolha == '3':
        remover_item()
    elif escolha == '4':
        calculo_total()
    elif escolha == '5':
        print("Obrigado por usar o programa de carrinho de compras. Tchau!")
        break
    else:
        print("Escolha inválida. Selecione uma opção válida.")
