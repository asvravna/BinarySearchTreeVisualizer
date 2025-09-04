import tkinter as tk
from tkinter import messagebox
from bst import BST
from view import BSTVisualizer
import random


class BSTInteractiveApp:
    def __init__(self, root):
        self.bst = BST()
        self.root = root
        self.root.title("Interactive BST")

        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()

        # Input frame
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        self.entry = tk.Entry(self.frame, width=10)
        self.entry.pack(side=tk.LEFT)

        # Insert button
        self.insert_button = tk.Button(self.frame, text="Insert", command=self.insert_value)
        self.insert_button.pack(side=tk.LEFT)

        # Remove button
        self.remove_button = tk.Button(self.frame, text="Remove", command=self.remove_value)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.entry.focus()
        self.entry.bind("<Return>", lambda event: self.insert_value())

        # Random insert button
        self.random_button = tk.Button(
            self.frame, 
            text="Insert 10 Random", 
            command=self.insert_random_numbers_animated
        )
        self.random_button.pack(side=tk.LEFT, padx=5)

        # Clear button
        self.clear_button = tk.Button(
            self.frame, 
            text="Clear", 
            command=self.clear_tree
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Visualizer
        self.visualizer = BSTVisualizer(self.bst, self.canvas)

    # ----------------- Insert -----------------
    def insert_value(self):
        val = self.entry.get()
        if not val.isdigit():
            messagebox.showerror("Invalid input", "Please enter an integer")
            return
        val = int(val)
        self.bst.insert(val)
        self.entry.delete(0, tk.END)
        self.visualizer.redraw()

    # ----------------- Remove -----------------
    def remove_value(self):
        val = self.entry.get()
        if not val.isdigit():
            messagebox.showerror("Invalid input", "Please enter an integer")
            return
        val = int(val)
        if not self.bst.contains(val):
            messagebox.showinfo("Not found", f"Value {val} is not in the tree")
        else:
            # Highlight the node to remove
            self.visualizer.highlight_value = val
            self.visualizer.redraw()
            # Wait 500ms before actual removal
            self.root.after(500, lambda: self._do_remove(val))
        self.entry.delete(0, tk.END)

    def _do_remove(self, val):
        self.bst.remove(val)
        self.visualizer.highlight_value = None
        self.visualizer.redraw()

    # ----------------- Random insert -----------------
    def insert_random_numbers_animated(self, count=10, lower=1, upper=100, delay=800):
        numbers = [random.randint(lower, upper) for _ in range(count)]

        def insert_next(i):
            if i < len(numbers):
                self.bst.insert(numbers[i])
                self.visualizer.redraw()
                self.root.after(delay, lambda: insert_next(i + 1))

        insert_next(0)

    # ----------------- Clear tree -----------------
    def clear_tree(self):
        self.bst = BST()
        self.visualizer.bst = self.bst
        self.visualizer.redraw()


