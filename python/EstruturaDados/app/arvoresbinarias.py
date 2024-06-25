class No:
    def __init__(self, chave):
        self.esquerda = None
        self.direita = None
        self.chave = chave

def inserir(raiz, chave):
    if raiz is None:
        return No(chave)
    else:
        if chave < raiz.chave:
            raiz.esquerda = inserir(raiz.esquerda, chave)
        else:
            raiz.direita = inserir(raiz.direita, chave)
    return raiz

def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.chave, end=' ')
        em_ordem(raiz.direita)

# Demonstração de Árvore Binária
raiz = None
valores = [10, 5, 20, 3, 7, 15, 25]
for valor in valores:
    raiz = inserir(raiz, valor)

print("Árvore binária em ordem:")
em_ordem(raiz)
