class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)

    def mostrar_grafo(self):
        for vertice in self.grafo:
            print(vertice, ":", self.grafo[vertice])

def bfs(grafo, vertice_inicial):
    visitados = []
    fila = [vertice_inicial]

    while fila:
        vertice = fila.pop(0)
        if vertice not in visitados:
            visitados.append(vertice)
            fila.extend([v for v in grafo[vertice] if v not in visitados])
    
    return visitados

def dfs(grafo, vertice_inicial, visitados=None):
    if visitados is None:
        visitados = []
    
    visitados.append(vertice_inicial)
    for vizinho in grafo[vertice_inicial]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
    
    return visitados

# Criando o grafo e adicionando vértices e arestas
g = Grafo()
vertices = ['A', 'B', 'C', 'D', 'E']
for vertice in vertices:
    g.adicionar_vertice(vertice)

arestas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
for aresta in arestas:
    g.adicionar_aresta(*aresta)

# Exibindo o grafo
g.mostrar_grafo()

# Realizando BFS e DFS a partir do vértice 'A'
print("Busca em Largura (BFS) a partir do vértice 'A':")
print(bfs(g.grafo, 'A'))

print("Busca em Profundidade (DFS) a partir do vértice 'A':")
print(dfs(g.grafo, 'A'))

# Verificando a conectividade de todos os vértices
todos_conectados = len(bfs(g.grafo, 'A')) == len(vertices)
print("Todos os vértices estão conectados?", todos_conectados)
