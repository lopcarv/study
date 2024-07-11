# Aula_Exame_Sesc 2024 by: Luis Orlando

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    else:
        if valor < raiz.valor:
            raiz.esquerda = inserir(raiz.esquerda, valor)
        else:
            raiz.direita = inserir(raiz.direita, valor)
    return raiz

def em_ordem(no):
    if no is not None:
        em_ordem(no.esquerda)
        print(no.valor, end=" ")
        em_ordem(no.direita)

def pre_ordem(no):
    if no is not None:
        print(no.valor, end=" ")
        pre_ordem(no.esquerda)
        pre_ordem(no.direita)

def pos_ordem(no):
    if no is not None:
        pos_ordem(no.esquerda)
        pos_ordem(no.direita)
        print(no.valor, end=" ")

def buscar(raiz, valor):
    if raiz is None or raiz.valor == valor:
        return raiz is not None
    if valor < raiz.valor:
        return buscar(raiz.esquerda, valor)
    else:
        return buscar(raiz.direita, valor)

# Criando a árvore e inserindo valores
raiz = None
valores = [10, 5, 15, 3, 7, 12, 18]
for valor in valores:
    raiz = inserir(raiz, valor)

# Exibindo os percursos
print("Percurso em ordem:")
em_ordem(raiz)
print("\nPercurso pré-ordem:")
pre_ordem(raiz)
print("\nPercurso pós-ordem:")
pos_ordem(raiz)

# Buscando um valor na árvore
valor_buscar = 7
if buscar(raiz, valor_buscar):
    print(f"\nValor {valor_buscar} encontrado na árvore.")
else:
    print(f"\nValor {valor_buscar} não encontrado na árvore.")
