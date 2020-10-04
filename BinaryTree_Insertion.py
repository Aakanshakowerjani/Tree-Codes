class BinaryTree:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def add_left_node(self, data):
        self.left_node = BinaryTree(data)
        return self.left_node

    def add_right_node(self, data):
        self.right_node = BinaryTree(data)
        return self.right_node

    def printInorder(self):
        if self.left_node != None:
            self.left_node.printInorder()
        print(self.data,end=" ")
        if self.right_node != None:
            self.right_node.printInorder()

    def printPreorder(self):
        print(self.data,end=" ")
        if self.left_node != None:
            self.left_node.printInorder()
        if self.right_node != None:
            self.right_node.printInorder()

    def printPostorder(self):
        if self.left_node != None:
            self.left_node.printInorder()
        if self.right_node != None:
            self.right_node.printInorder()
        print(self.data,end=" ")


def main():
    root = BinaryTree(7)
    left = root.add_left_node(8)
    right = root.add_right_node(9)
    left.add_left_node(5)
    left.add_right_node(4)
    right.add_left_node(2)
    right.add_right_node(1)
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
