class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # ---------- INSERT ----------
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        return node

    # ---------- REMOVE ----------
    def remove(self, value):
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def _remove(node, value):
            if node is None:
                return None
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:  # found node
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # two children: replace with min from right subtree
                u = find_min(node.right)
                node.value = u.value
                node.right = _remove(node.right, u.value)
            return node

        self.root = _remove(self.root, value)

    # ---------- SEARCH ----------
    def search(self, value):
        def _search(node, value):
            if node is None:
                return None
            if value == node.value:
                return node
            elif value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    # ---------- SIZE ----------
    def size(self):
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    # ---------- CONTAINS (bool) ----------
    def contains(self, value):
        return self.search(value) is not None

