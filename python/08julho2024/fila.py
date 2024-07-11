# Exemplo de Fila em Python
from collections import deque

queue = deque(['Idosa', 'Mulher', 'Homem'])
queue.append('Menino')
print("Fila (após enfileirar Menino):", queue)
print("Elemento desenfileirado:", queue.popleft())
print("Fila após desenfileirar:", queue)