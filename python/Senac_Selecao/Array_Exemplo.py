# Aula_Exame_Sesc 2024 by: Luis Orlando
# Passo 1: Criando um array de números inteiros
array = [5, 10, 15, 20, 25]

# Passo 2: Acessando e imprimindo o segundo e o último elemento do array
print("Segundo elemento:", array[1])
print("Último elemento:", array[-1])

# Passo 3: Modificando o valor do quarto elemento
array[3] = 18
print("Array após modificação:", array)

# Passo 4: Iterando sobre o array e imprimindo cada elemento
print("Elementos do array:")
for elemento in array:
    print(elemento)

# Passo 5: Adicionando um novo elemento no início do array e removendo o terceiro elemento
array.insert(0, 2)
print("Array após adicionar elemento no início:", array)
array.pop(2)
print("Array após remover o terceiro elemento:", array)