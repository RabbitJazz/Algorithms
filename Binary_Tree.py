### Binary Tree Implementation ###

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def pre_order_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.data + "->"))
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += str(start.data + "->")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.data + "->"))
        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "pre_order":
            return self.pre_order_print(tree_1.root, " ")
        elif traversal_type == "post_order":
            return self.post_order_print(tree_1.root, " ")
        elif traversal_type == "in_order":
            return self.in_order_print(tree_1.root, " ")
        else:
            print(f"Traversal type {traversal_type} is not supported")


def what3(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 0
    if tree.right is None:
        return 1 + what3(tree.left)
    if tree.left is None:
        return -1 + what3(tree.right)
    return what3(tree.left) + what3(tree.right)


def what4(tree, X, Y):
    if tree:
        print(f"{tree.data}\t{Y}")
        if X == 1:
            what4(tree.left, 0, Y + 1)
            what4(tree.right, 0, Y + 1)
        else:
            what4(tree.right, 1, Y + 1)
            what4(tree.left, 1, Y + 1)


# Example of Tree 1:
tree_1 = BinaryTree('A')
tree_1.root.left = Node('B')
tree_1.root.left.right = Node('E')
tree_1.root.left.left = Node('D')
tree_1.root.left.left.right = Node('H')
tree_1.root.left.left.left = Node('G')
tree_1.root.left.left.left.left = Node('K')
tree_1.root.right = Node('C')
tree_1.root.right.right = Node('F')
tree_1.root.right.right.right = Node('J')
tree_1.root.right.right.left = Node('I')
tree_1.root.right.right.left.right = Node('M')
tree_1.root.right.right.left.left = Node('L')

# what(tree, 1, 1)
print("Pre-order traversal:" + tree_1.print_tree("pre_order") + "end")
print("In-order traversal:" + tree_1.print_tree("in_order") + "end")
print("Post-order traversal :" + tree_1.print_tree("post_order") + "end")

print(what3(tree_1.root))
