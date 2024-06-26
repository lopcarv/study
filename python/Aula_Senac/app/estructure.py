import tkinter as tk
from collections import deque

# Funções para manipulação de estruturas de dados
def adicionar_lista():
    valor = entry_lista.get()
    if valor:
        lista.append(valor)
        atualizar_lista()

def remover_lista():
    if lista:
        lista.pop()
        atualizar_lista()

def atualizar_lista():
    label_lista.config(text="Lista: " + str(lista))

def adicionar_pilha():
    valor = entry_pilha.get()
    if valor:
        pilha.append(valor)
        atualizar_pilha()

def remover_pilha():
    if pilha:
        pilha.pop()
        atualizar_pilha()

def atualizar_pilha():
    label_pilha.config(text="Pilha: " + str(pilha))

def adicionar_fila():
    valor = entry_fila.get()
    if valor:
        fila.append(valor)
        atualizar_fila()

def remover_fila():
    if fila:
        fila.popleft()
        atualizar_fila()

def atualizar_fila():
    label_fila.config(text="Fila: " + str(fila))

def adicionar_conjunto():
    valor = entry_conjunto.get()
    if valor:
        conjunto.add(valor)
        atualizar_conjunto()

def remover_conjunto():
    valor = entry_conjunto.get()
    if valor in conjunto:
        conjunto.remove(valor)
        atualizar_conjunto()

def atualizar_conjunto():
    label_conjunto.config(text="Conjunto: " + str(conjunto))

def adicionar_dicionario():
    chave = entry_dicionario_chave.get()
    valor = entry_dicionario_valor.get()
    if chave and valor:
        dicionario[chave] = valor
        atualizar_dicionario()

def remover_dicionario():
    chave = entry_dicionario_chave.get()
    if chave in dicionario:
        del dicionario[chave]
        atualizar_dicionario()

def atualizar_dicionario():
    label_dicionario.config(text="Dicionário: " + str(dicionario))

# Inicialização das estruturas de dados
lista = []
pilha = []
fila = deque()
conjunto = set()
dicionario = {}

# Criação da janela principal
root = tk.Tk()
root.title("Demonstração de Estruturas de Dados by: Luis Orlando")

# Lista
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)
label_lista = tk.Label(frame_lista, text="Lista: " + str(lista))
label_lista.pack()
entry_lista = tk.Entry(frame_lista)
entry_lista.pack()
tk.Button(frame_lista, text="Adicionar", command=adicionar_lista).pack(side=tk.LEFT)
tk.Button(frame_lista, text="Remover", command=remover_lista).pack(side=tk.LEFT)

# Pilha
frame_pilha = tk.Frame(root)
frame_pilha.pack(pady=10)
label_pilha = tk.Label(frame_pilha, text="Pilha: " + str(pilha))
label_pilha.pack()
entry_pilha = tk.Entry(frame_pilha)
entry_pilha.pack()
tk.Button(frame_pilha, text="Adicionar", command=adicionar_pilha).pack(side=tk.LEFT)
tk.Button(frame_pilha, text="Remover", command=remover_pilha).pack(side=tk.LEFT)

# Fila
frame_fila = tk.Frame(root)
frame_fila.pack(pady=10)
label_fila = tk.Label(frame_fila, text="Fila: " + str(fila))
label_fila.pack()
entry_fila = tk.Entry(frame_fila)
entry_fila.pack()
tk.Button(frame_fila, text="Adicionar", command=adicionar_fila).pack(side=tk.LEFT)
tk.Button(frame_fila, text="Remover", command=remover_fila).pack(side=tk.LEFT)

# Conjunto
frame_conjunto = tk.Frame(root)
frame_conjunto.pack(pady=10)
label_conjunto = tk.Label(frame_conjunto, text="Conjunto: " + str(conjunto))
label_conjunto.pack()
entry_conjunto = tk.Entry(frame_conjunto)
entry_conjunto.pack()
tk.Button(frame_conjunto, text="Adicionar", command=adicionar_conjunto).pack(side=tk.LEFT)
tk.Button(frame_conjunto, text="Remover", command=remover_conjunto).pack(side=tk.LEFT)

# Dicionário
frame_dicionario = tk.Frame(root)
frame_dicionario.pack(pady=10)
label_dicionario = tk.Label(frame_dicionario, text="Dicionário: " + str(dicionario))
label_dicionario.pack()
entry_dicionario_chave = tk.Entry(frame_dicionario)
entry_dicionario_chave.pack()
entry_dicionario_valor = tk.Entry(frame_dicionario)
entry_dicionario_valor.pack()
tk.Button(frame_dicionario, text="Adicionar", command=adicionar_dicionario).pack(side=tk.LEFT)
tk.Button(frame_dicionario, text="Remover", command=remover_dicionario).pack(side=tk.LEFT)

# Executa a aplicação
root.mainloop()
