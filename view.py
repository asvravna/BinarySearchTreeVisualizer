import tkinter as tk

class BSTVisualizer:
    def __init__(self, bst, root):
        self.bst = bst
        self.window = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.highlight_value = None  # value to highlight

    def redraw(self):
        self.canvas.delete("all")
        if self.bst.root:
            self.draw_tree(self.bst.root, 400, 50, 150)

    def draw_tree(self, node, x, y, dx):
        if node:
            fill_color = 'red' if node.value == self.highlight_value else 'lightblue'
            self.canvas.create_oval(x-15, y-15, x+15, y+15, fill=fill_color)
            self.canvas.create_text(x, y, text=str(node.value))
            if node.left:
                self.canvas.create_line(x, y+15, x-dx, y+60-15)
                self.draw_tree(node.left, x-dx, y+60, dx/2)
            if node.right:
                self.canvas.create_line(x, y+15, x+dx, y+60-15)
                self.draw_tree(node.right, x+dx, y+60, dx/2)
