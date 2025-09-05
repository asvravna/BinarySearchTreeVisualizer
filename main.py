import tkinter as tk
from interactive import BSTInteractiveApp
from bst import BST
from view import BSTVisualizer

def main():
    root = tk.Tk()
    app = BSTInteractiveApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    root = tk.Tk()
    bst = BST()
    bst.insert(10)
    bst.insert(20)

    bst.insert(5)

    visualizer = BSTVisualizer(bst, root)
    visualizer.redraw()

    btn_to_avl = tk.Button(root, text="Transform to AVL", command=visualizer.transform_to_avl)
    btn_to_avl.pack()

    root.mainloop()
