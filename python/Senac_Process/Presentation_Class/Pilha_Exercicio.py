# Aula_Exame_Sesc 2024 by: Luis Orlando
# Passo 1: Criando uma pilha de números inteiros
pilha = []

# Passo 2: Adicionando cinco elementos à pilha
pilha.append(10)
pilha.append(20)
pilha.append(30)
pilha.append(40)
pilha.append(50)

# Imprimindo a pilha após adições
print("Pilha após empilhar elementos:", pilha)

# Passo 3: Removendo dois elementos da pilha
pilha.pop()
pilha.pop()

# Imprimindo a pilha após remoções
print("Pilha após desempilhar elementos:", pilha)

# Passo 4: Imprimindo o último elemento restante na pilha
ultimo_elemento = pilha[-1]
print("Último elemento da pilha:", ultimo_elemento)

# Passo 5: Iterando sobre a pilha e imprimindo cada elemento
print("Elementos restantes na pilha:")
for elemento in pilha:
    print(elemento)
