import networkx as nx

# Criando um grafo direcionado
G = nx.DiGraph()

# Adicionando vértices ao grafo
G.add_nodes(['A', 'B', 'C', 'D'])

# Adicionando arestas ao grafo
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'D')])

# Mostrando o grafo
print(nx.info(G))

# Verificando se existe um caminho entre dois vértices
print(nx.has_path(G, 'A', 'D'))

# Calculando a distância entre dois vértices
print(nx.shortest_path_length(G, 'A', 'D'))