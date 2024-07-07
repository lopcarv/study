import tkinter as tk
from tkinter import ttk

class DataStructuresVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Visualizador de Estruturas de Dados")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        self.frames = {}
        for name in ["Array", "Fila", "Pilha", "Lista", "Árvore", "Grafo"]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=name)
            self.frames[name] = frame

        self.create_array_frame()
        self.create_queue_frame()
        self.create_stack_frame()
        self.create_list_frame()
        self.create_tree_frame()
        self.create_graph_frame()

    def create_array_frame(self):
        frame = self.frames["Array"]
        label = ttk.Label(frame, text="Array: [1, 2, 3, 4, 5]", font=("Helvetica", 14))
        label.pack(pady=20)

    def create_queue_frame(self):
        frame = self.frames["Fila"]
        label = ttk.Label(frame, text="Fila: 1 <- 2 <- 3 <- 4 <- 5", font=("Helvetica", 14))
        label.pack(pady=20)

    def create_stack_frame(self):
        frame = self.frames["Pilha"]
        label = ttk.Label(frame, text="Pilha: [1, 2, 3, 4, 5] <- topo", font=("Helvetica", 14))
        label.pack(pady=20)

    def create_list_frame(self):
        frame = self.frames["Lista"]
        label = ttk.Label(frame, text="Lista: 1 -> 2 -> 3 -> 4 -> 5", font=("Helvetica", 14))
        label.pack(pady=20)

    def create_tree_frame(self):
        frame = self.frames["Árvore"]
        canvas = tk.Canvas(frame, width=400, height=400)
        canvas.pack(pady=20)

        # Desenhando uma árvore binária simples
        canvas.create_oval(180, 20, 220, 60, fill="lightblue")
        canvas.create_text(200, 40, text="10")

        canvas.create_oval(80, 100, 120, 140, fill="lightblue")
        canvas.create_text(100, 120, text="5")

        canvas.create_oval(280, 100, 320, 140, fill="lightblue")
        canvas.create_text(300, 120, text="15")

        canvas.create_line(200, 60, 100, 100)
        canvas.create_line(200, 60, 300, 100)

    def create_graph_frame(self):
        frame = self.frames["Grafo"]
        canvas = tk.Canvas(frame, width=400, height=400)
        canvas.pack(pady=20)

        # Desenhando um grafo simples
        nodes = {"A": (100, 100), "B": (300, 100), "C": (100, 300), "D": (300, 300)}
        edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]

        for node, pos in nodes.items():
            canvas.create_oval(pos[0]-20, pos[1]-20, pos[0]+20, pos[1]+20, fill="lightgreen")
            canvas.create_text(pos[0], pos[1], text=node)

        for edge in edges:
            pos1 = nodes[edge[0]]
            pos2 = nodes[edge[1]]
            canvas.create_line(pos1[0], pos1[1], pos2[0], pos2[1])

if __name__ == "__main__":
    app = DataStructuresVisualizer()
    app.mainloop()
