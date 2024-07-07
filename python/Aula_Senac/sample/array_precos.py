precos_produtos = [25.90, 18.50, 39.90, 79.90, 12.90]

# Acessando o preço do 3º produto:
terceiro_produto = precos_produtos[2]  # 39.90

# Atualizando o preço do 1º produto:
precos_produtos[0] = 23.50

# Mostrando todos os preços:
'''Descrição:

* for i, preco in enumerate(precos_produtos): Este loop percorre a lista precos_produtos. A função enumerate retorna tanto o índice (i) quanto o valor (preco) de cada item na lista.
* print(f"Produto {i+1}: R${preco:.2f}"): Esta linha imprime o número do produto (i+1) e seu preço formatado com duas casas decimais (:.2f).'''
for i, preco in enumerate(precos_produtos):
    print(f"Produto {i+1}: R${preco:.2f}")
