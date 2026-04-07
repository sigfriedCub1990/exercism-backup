class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode(data={self.data}, left={self.left}, right={self.right})"

    def __gt__(self, other):
        """
        Allow TreeNode N1 > N2 comparison
        """
        return int(self.data) > int(other.data)


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        for i in range(len(tree_data)):
            self._insert(TreeNode(tree_data[i]))

    def data(self):
        # Pre-order traversal to return items as they were inserted
        nodes = []
        self._pre_order(self.root, nodes)
        return nodes[len(nodes) - 1]

    def sorted_data(self):
        # In-order traversal to return items in ascending order
        sorted = []
        self._in_order(self.root, sorted)
        return sorted

    def _insert(self, node):
        """
        Insert a value in the BST

        data: Value to be inserted
        """
        inserted = False

        if self.root is None:  # If this is the first Node, insert it
            self.root = node
            inserted = True

        current = self.root

        while not inserted:
            if node > current:  # Move to right subtree
                if current.right == None:
                    current.right = node
                    inserted = True
                else:
                    current = current.right
            else:  # Move to left subtree
                if current.left == None:
                    current.left = node
                    inserted = True
                else:
                    current = current.left

    def _pre_order(self, root, nodes):
        if root is not None:
            nodes.append(self.root)
            self._pre_order(root.left, nodes)
            self._pre_order(root.right, nodes)

    def _in_order(self, root, sorted):
        if root is not None:
            self._in_order(root.left, sorted)
            sorted.append(root.data)
            self._in_order(root.right, sorted)
