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
        self.insert_button = tk.Button(self.frame, text="Insert", command=self.insert_value)
        self.insert_button.pack(side=tk.LEFT)
        self.entry.focus()
        self.entry.bind("<Return>", lambda event: self.insert_value())


        self.random_button = tk.Button(
            self.frame, 
            text="Insert 10 Random", 
            command=self.insert_random_numbers_animated
        )
        self.random_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(
            self.frame, 
            text="Clear", 
            command=self.clear_tree
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Visualizer
        self.visualizer = BSTVisualizer(self.bst, self.canvas)

    def insert_value(self):
        val = self.entry.get()
        if not val.isdigit():
            messagebox.showerror("Invalid input", "Please enter an integer")
            return
        val = int(val)
        self.bst.insert(val)
        self.entry.delete(0, tk.END)
        self.visualizer.redraw()

    def insert_random_numbers_animated(self, count=10, lower=1, upper=100, delay=800):
        """Insert `count` random numbers one by one with a delay (milliseconds)."""
        numbers = [random.randint(lower, upper) for _ in range(count)]

        def insert_next(i):
            if i < len(numbers):
                self.bst.insert(numbers[i])
                self.visualizer.redraw()
                # Schedule the next insertion
                self.root.after(delay, lambda: insert_next(i + 1))

        insert_next(0)


    def insert_random_numbers(self, count=10, lower=1, upper=100):
        for _ in range(count):
            val = random.randint(lower, upper)
            self.bst.insert(val)
        self.visualizer.redraw()

    def clear_tree(self):
        self.bst = BST()          # Reset the BST
        self.visualizer.bst = self.bst  # Update the visualizer
        self.visualizer.redraw()  # Clear the canvas


