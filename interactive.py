import tkinter as tk
from tkinter import messagebox
from bst import BST
from avl import AVLTree 
from view import BSTVisualizer
import random


class BSTInteractiveApp:
    def __init__(self, root):
        self.bst = BST()
        self.root = root
        self.root.title("Interactive BST")

        self.canvas = tk.Canvas(root, width=800, height=600, bg='pink')
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

        self.avl_button = tk.Button(
            self.frame,
            text="AVL",
            command=self.transform_to_avl
        )
        self.avl_button.pack(side=tk.LEFT, padx=5)

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
            self.visualizer.highlight_value = val
            self.visualizer.redraw()
            self.root.after(500, lambda: self._do_remove(val))
        self.entry.delete(0, tk.END)

    def _do_remove(self, val):
        self.bst.remove(val)
        self.visualizer.highlight_value = None
        self.visualizer.redraw()

    # ----------------- Random insert -----------------
    def insert_random_numbers_animated(self, count=10, lower=1, upper=100, delay=500):
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

    # ----------------- Transform to AVL -----------------
    def transform_to_avl(self):
        from avl import get_balance, rotate_left, rotate_right, update_height

        def redraw_callback():
            self.visualizer.redraw()
            self.root.update()
            # small delay for animation
            self.root.after(400)

        def balance_post_order(node):
            if node is None:
                return None

            # First, balance children
            node.left = balance_post_order(node.left)
            node.right = balance_post_order(node.right)

            # Update height
            update_height(node)

            # Check balance
            balance = get_balance(node)

            # Left heavy
            if balance > 1:
                if get_balance(node.left) < 0:
                    node.left = rotate_left(node.left, redraw_callback)
                node = rotate_right(node, redraw_callback)

            # Right heavy
            elif balance < -1:
                if get_balance(node.right) > 0:
                    node.right = rotate_right(node.right, redraw_callback)
                node = rotate_left(node, redraw_callback)

            redraw_callback()  # redraw after balancing this node
            return node

        # Start balancing from the root
        self.bst.root = balance_post_order(self.bst.root)
