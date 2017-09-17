# One root node (head)
# each node can only have one parent, only one path to node can exist

class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = BinarySearchTreeNode(value)
        if self.root == None:
            self.root = new_node
        else:
            self.add_r(self.root, new_node)
    
    def add_r(self, node, new_node):
        if new_node.value < node.value:
            if node.left == None:
                node.left = new_node
                new_node.parent = node
            else:
                self.add_r(node.left, new_node)
        else:
            if node.right == None:
                node.right = new_node
                new_node.parent = node
            else:
                self.add_r(node.right, new_node)
    
    def print_preorder(self):
        if self.root is not None:
            self.preorder_r(self.root)

    def preorder_r(self, node):
        print(node.value)
        if node.left is not None:
            self.preorder_r(node.left)
        if node.right is not None:
            self.preorder_r(node.right)



tree = BinarySearchTree()
tree.add(50)
tree.add(37)
tree.add(88)
tree.add(64)
tree.add(22)
tree.add(33)
tree.print_preorder()