class BST:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def add_node(self, data):
        if self.data <= data:
            if self.right_node != None:
                self.right_node.add_node(data)
            else:
                self.right_node = BST(data)
        else:
            if self.left_node != None:
                self.left_node.add_node(data)
            else:
                self.left_node = BST(data)

    def printInorder(self):
        if self.left_node != None:
            self.left_node.printInorder()
        print(self.data, end=" ")
        if self.right_node != None:
            self.right_node.printInorder()

    def printPreorder(self):
        print(self.data, end=" ")
        if self.left_node != None:
            self.left_node.printPreorder()
        if self.right_node != None:
            self.right_node.printPreorder()

    def printPostorder(self):
        if self.left_node != None:
            self.left_node.printPostorder()
        if self.right_node != None:
            self.right_node.printPostorder()
        print(self.data, end=" ")


def main():
    root = BST(int(input("enter root node")))
    nodes = list(map(int, input("enter random nodes").split()))
    for node in nodes:
        root.add_node(node)
    print('INORDER TRAVERSAL')
    root.printInorder()
    print()
    print('PREORDER TRAVERSAL')
    root.printPreorder()
    print()
    print('POSTORDER TRAVERSAL')
    root.printPostorder()
    
if __name__ == "__main__":
    main()
