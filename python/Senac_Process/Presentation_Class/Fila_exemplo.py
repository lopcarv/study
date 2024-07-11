# Aula_Exame_Sesc 2024 by: Luis Orlando
from collections import deque

# Passo 1: Criando uma fila de números inteiros
fila = deque()

# Passo 2: Adicionando cinco elementos à fila
fila.append(10)
fila.append(20)
fila.append(30)
fila.append(40)
fila.append(50)

# Imprimindo a fila após adições
print("Fila após adicionar elementos:", fila)

# Passo 3: Removendo dois elementos da fila
fila.popleft()
fila.popleft()

# Imprimindo a fila após remoções
print("Fila após remover elementos:", fila)

# Passo 4: Imprimindo o primeiro e o último elemento restantes na fila
print("Primeiro elemento da fila:", fila[0])
print("Último elemento da fila:", fila[-1])

# Passo 5: Iterando sobre a fila e imprimindo cada elemento
print("Elementos restantes na fila:")
for elemento in fila:
    print(elemento)