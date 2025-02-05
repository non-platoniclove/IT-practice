class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
Class BinaryTree:
    def insert(self, root, data):
        if root is None:
            return BinaryTreeNode(data)
    
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
            
        return root
    def deleteNode(self, root, data):
        if root is None:
            return root
            
        if data < root.data:
            root.left = self.deleteNode(root.left, data)
        elif data > root.data:
            root.right = self.deleteNode(root.right,data)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.data = self.getMin(root.right).data
                root.right = self.deleteNode(root.right, root.data)
        return root
    
    def getMin(self, root):
        if root is None:
            return root
            
        while root.left is not None:
            root = root.left
        return root