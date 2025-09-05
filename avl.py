from bst import Node, BST


class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1  # a new node is a leaf with height 1

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    return get_height(node.left) - get_height(node.right)


# def rotate_right(y):
#     x = y.left
#     T2 = x.right

#     # Perform rotation
#     x.right = y
#     y.left = T2

#     # Update heights
#     update_height(y)
#     update_height(x)

#     return x  # new root
def rotate_right(y, redraw_callback=None):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Update heights
    update_height(y)
    update_height(x)

    if redraw_callback:
        redraw_callback()

    return x


def rotate_left(x, redraw_callback=None):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    update_height(x)
    update_height(y)

    if redraw_callback:
        redraw_callback()

    return y


# def rotate_left(x):
#     y = x.right
#     T2 = y.left

#     # Perform rotation
#     y.left = x
#     x.right = T2

#     # Update heights
#     update_height(x)
#     update_height(y)

#     return y  # new root
def rotate_left(x, redraw_callback=None):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Update heights
    update_height(x)
    update_height(y)

    if redraw_callback:
        redraw_callback()

    return y

class AVLTree(BST):
    def _insert(self, node, value):
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # no duplicates

        # Update height
        update_height(node)

        # Balance the node
        balance = get_balance(node)

        # Case 1: Left Left
        if balance > 1 and value < node.left.value:
            return rotate_right(node)

        # Case 2: Right Right
        if balance < -1 and value > node.right.value:
            return rotate_left(node)

        # Case 3: Left Right
        if balance > 1 and value > node.left.value:
            node.left = rotate_left(node.left)
            return rotate_right(node)

        # Case 4: Right Left
        if balance < -1 and value < node.right.value:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node
