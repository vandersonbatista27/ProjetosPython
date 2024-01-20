# Neste programa o usuário informará os preços da refeição infantil e o preço da refeição do adulto
valor_adulto = float(input(f"Qual o preço da refeição de um adulto? "))
valor_crianca = float(input(f"Qual o preço da refeição de uma criança? "))

numero_de_adultos = int(input(f"Quantos adultos existem? "))
numero_de_criancas = int(input(f"Quantas crianças existem? "))

# Agora calcule o subtotal
subtotal = (numero_de_criancas * valor_crianca) + \
    (numero_de_adultos * valor_adulto)

# Exibir o subtotal
print(f"Subtotal: R${subtotal:.2f}")

# Taxa de imposto
taxa_de_imposto = float(
    input(f"Qual é a taxa de imposto sobre a venda (em porcentagem)? "))

# Cálculo da Taxa de imposto
taxa_imposto = (subtotal * taxa_de_imposto) / 100

# Cálculo do preço total da refeição
preco_total = subtotal + taxa_imposto

# Exibir o imposto sobre vendas e o total com o símbolo da moeda e duas casas decimais
print(f"imposto sobre a venda: R${taxa_imposto:.2f}")
print(f"Total: R${preco_total:.2f}")

# Solicite ao usuário o valor do pagamento
valor_do_pagamento = float(input(f"Quanto irá pagar? R$"))

# Cálculo do troco
troco = valor_do_pagamento - preco_total

# Exibir o troco com o símbolo da moeda e duas casas decimais
print(f"Troco: R${troco:.2f}")
