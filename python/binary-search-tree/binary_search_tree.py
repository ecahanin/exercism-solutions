class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree:
    def __init__(self, tree_data):
        self.tree = TreeNode(tree_data[0])
        for x in tree_data[1:]:
            self.add_to_tree(x, self.tree)

    def add_to_tree(self, x, node):
        if x <= node.data:
            if node.left:
                self.add_to_tree(x, node.left)
            else:
                node.left = TreeNode(x)
        elif x > node.data:
            if node.right:
                self.add_to_tree(x, node.right)
            else:
                node.right = TreeNode(x)
        
    def data(self):
        return self.tree

    def sorted_data(self):
        return self.read_node(self.tree)
        
    def read_node(self, node):
        left_data, right_data = ([],[])
        if node.left is not None:
            left_data = self.read_node(node.left)
        if node.right is not None:
            right_data = self.read_node(node.right)
        data = left_data + list(node.data) + right_data
        return data

        
