import tkinter as tk
from tkinter import ttk

class DataStructuresVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ED VIEW")
        self.geometry("800x600")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)

        self.frames = {}
        for name in ["Array", "Fila", "Pilha", "Lista", "Árvore", "Grafo"]:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=name)
            self.frames[name] = frame

        self.array = []
        self.queue = []
        self.stack = []
        self.linked_list = []
        self.tree = None
        self.graph = {"nodes": {}, "edges": []}

        self.create_array_frame()
        self.create_queue_frame()
        self.create_stack_frame()
        self.create_list_frame()
        self.create_tree_frame()
        self.create_graph_frame()

    def create_array_frame(self):
        frame = self.frames["Array"]
        self.array_label = ttk.Label(frame, text="Array: []", font=("Helvetica", 14))
        self.array_label.pack(pady=20)

        self.array_entry = ttk.Entry(frame)
        self.array_entry.pack(pady=5)

        self.array_add_button = ttk.Button(frame, text="Adicionar", command=self.add_to_array)
        self.array_add_button.pack(pady=5)

    def add_to_array(self):
        value = self.array_entry.get()
        if value:
            self.array.append(value)
            self.update_array_label()

    def update_array_label(self):
        self.array_label.config(text=f"Array: {self.array}")

    def create_queue_frame(self):
        frame = self.frames["Fila"]
        self.queue_label = ttk.Label(frame, text="Fila: []", font=("Helvetica", 14))
        self.queue_label.pack(pady=20)

        self.queue_entry = ttk.Entry(frame)
        self.queue_entry.pack(pady=5)

        self.queue_add_button = ttk.Button(frame, text="Adicionar", command=self.add_to_queue)
        self.queue_add_button.pack(pady=5)

        self.queue_remove_button = ttk.Button(frame, text="Remover", command=self.remove_from_queue)
        self.queue_remove_button.pack(pady=5)

    def add_to_queue(self):
        value = self.queue_entry.get()
        if value:
            self.queue.append(value)
            self.update_queue_label()

    def remove_from_queue(self):
        if self.queue:
            self.queue.pop(0)
            self.update_queue_label()

    def update_queue_label(self):
        self.queue_label.config(text=f"Fila: {' <- '.join(self.queue)}")

    def create_stack_frame(self):
        frame = self.frames["Pilha"]
        self.stack_label = ttk.Label(frame, text="Pilha: []", font=("Helvetica", 14))
        self.stack_label.pack(pady=20)

        self.stack_entry = ttk.Entry(frame)
        self.stack_entry.pack(pady=5)

        self.stack_add_button = ttk.Button(frame, text="Adicionar", command=self.add_to_stack)
        self.stack_add_button.pack(pady=5)

        self.stack_remove_button = ttk.Button(frame, text="Remover", command=self.remove_from_stack)
        self.stack_remove_button.pack(pady=5)

    def add_to_stack(self):
        value = self.stack_entry.get()
        if value:
            self.stack.append(value)
            self.update_stack_label()

    def remove_from_stack(self):
        if self.stack:
            self.stack.pop()
            self.update_stack_label()

    def update_stack_label(self):
        self.stack_label.config(text=f"Pilha: {self.stack} <- topo")

    def create_list_frame(self):
        frame = self.frames["Lista"]
        self.list_label = ttk.Label(frame, text="Lista: []", font=("Helvetica", 14))
        self.list_label.pack(pady=20)

        self.list_entry = ttk.Entry(frame)
        self.list_entry.pack(pady=5)

        self.list_add_button = ttk.Button(frame, text="Adicionar", command=self.add_to_list)
        self.list_add_button.pack(pady=5)

    def add_to_list(self):
        value = self.list_entry.get()
        if value:
            self.linked_list.append(value)
            self.update_list_label()

    def update_list_label(self):
        self.list_label.config(text=f"Lista: {' -> '.join(self.linked_list)}")

    def create_tree_frame(self):
        frame = self.frames["Árvore"]
        self.tree_canvas = tk.Canvas(frame, width=400, height=400)
        self.tree_canvas.pack(pady=20)

        self.tree_entry = ttk.Entry(frame)
        self.tree_entry.pack(pady=5)

        self.tree_add_button = ttk.Button(frame, text="Adicionar", command=self.add_to_tree)
        self.tree_add_button.pack(pady=5)

    def add_to_tree(self):
        value = self.tree_entry.get()
        if value:
            if not self.tree:
                self.tree = TreeNode(value)
            else:
                self.insert_into_tree(self.tree, value)
            self.update_tree_canvas()

    def insert_into_tree(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.insert_into_tree(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.insert_into_tree(node.right, value)

    def update_tree_canvas(self):
        self.tree_canvas.delete("all")
        if self.tree:
            self.draw_tree(self.tree, 200, 20, 100)

    def draw_tree(self, node, x, y, spacing):
        if node:
            self.tree_canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.tree_canvas.create_text(x, y, text=node.value)
            if node.left:
                self.tree_canvas.create_line(x, y+20, x-spacing, y+70)
                self.draw_tree(node.left, x-spacing, y+70, spacing//2)
            if node.right:
                self.tree_canvas.create_line(x, y+20, x+spacing, y+70)
                self.draw_tree(node.right, x+spacing, y+70, spacing//2)

    def create_graph_frame(self):
        frame = self.frames["Grafo"]
        self.graph_canvas = tk.Canvas(frame, width=400, height=400)
        self.graph_canvas.pack(pady=20)

        self.graph_node_entry = ttk.Entry(frame)
        self.graph_node_entry.pack(pady=5)

        self.graph_node_add_button = ttk.Button(frame, text="Adicionar Nó", command=self.add_node_to_graph)
        self.graph_node_add_button.pack(pady=5)

        self.graph_edge_entry = ttk.Entry(frame)
        self.graph_edge_entry.pack(pady=5)

        self.graph_edge_add_button = ttk.Button(frame, text="Adicionar Aresta", command=self.add_edge_to_graph)
        self.graph_edge_add_button.pack(pady=5)

    def add_node_to_graph(self):
        node = self.graph_node_entry.get()
        if node and node not in self.graph["nodes"]:
            self.graph["nodes"][node] = (len(self.graph["nodes"]) * 100 + 50, 200)
            self.update_graph_canvas()

    def add_edge_to_graph(self):
        edge = self.graph_edge_entry.get().split(",")
        if len(edge) == 2 and edge[0] in self.graph["nodes"] and edge[1] in self.graph["nodes"]:
            self.graph["edges"].append((edge[0], edge[1]))
            self.update_graph_canvas()

    def update_graph_canvas(self):
        self.graph_canvas.delete("all")
        for node, pos in self.graph["nodes"].items():
            self.graph_canvas.create_oval(pos[0]-20, pos[1]-20, pos[0]+20, pos[1]+20, fill="lightgreen")
            self.graph_canvas.create_text(pos[0], pos[1], text=node)

        for edge in self.graph["edges"]:
            pos1 = self.graph["nodes"][edge[0]]
            pos2 = self.graph["nodes"][edge[1]]
            self.graph_canvas.create_line(pos1[0], pos1[1], pos2[0], pos2[1])

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    app = DataStructuresVisualizer()
    app.mainloop()
