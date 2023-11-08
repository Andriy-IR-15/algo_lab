class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree: BinaryTree) -> BinaryTree:
    if tree is None:
        return None

    stack = [tree]

    while stack:
        current = stack.pop(0)
        current.left, current.right = current.right, current.left

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

        return tree

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

new_root = invert_binary_tree(root)


def print_tree(node, prefix=""):
    if node is not None:
        print(prefix + str(node.value))
        stack = [(node.left, prefix + "|--"), (node.right, prefix + "--")]
        while stack:
            current, current_prefix = stack.pop()
            if current:
                print(current_prefix + str(current.value))
                stack.append((current.left, current_prefix + "|--"))
                stack.append((current.right, current_prefix + "--"))


print_tree(new_root)
