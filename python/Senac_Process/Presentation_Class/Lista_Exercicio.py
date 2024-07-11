# Aula_Exame_Sesc 2024 by: Luis Orlando
# Passo 1: Criando uma lista de strings
lista = []

# Passo 2: Adicionando três elementos à lista
lista.append("maçã")
lista.append("banana")
lista.append("cereja")

# Imprimindo a lista após adições
print("Lista após adicionar elementos:", lista)

# Passo 3: Removendo o segundo elemento da lista
lista.remove("banana")

# Imprimindo a lista após remoção
print("Lista após remover um elemento:", lista)

# Passo 4: Imprimindo o primeiro e o último elemento da lista
print("Primeiro elemento da lista:", lista[0])
print("Último elemento da lista:", lista[-1])

# Passo 5: Iterando sobre a lista e imprimindo cada elemento
print("Elementos restantes na lista:")
for elemento in lista:
    print(elemento)
