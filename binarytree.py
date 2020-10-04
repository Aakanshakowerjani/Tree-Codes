class BinaryTree:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def print_inorder(self):

        if self.left_node != None:
            self.left_node.print_inorder()
        print(self.data, end=" ")
        if self.right_node != None:
            self.right_node.print_inorder()

    def print_postorder(self):
        if self.left_node != None:
            self.left_node.print_inorder()

        if self.right_node != None:
            self.right_node.print_inorder()

        print(self.data, end=" ")

    def print_preorder(self):
        print(self.data, end=" ")
        if self.left_node != None:
            self.left_node.print_inorder()

        if self.right_node != None:
            self.right_node.print_inorder()


class BinarySearchTree(BinaryTree):
    def __init__(self, data, left_node=None, right_node=None):
        super().__init__(data, left_node, right_node)

    def add_left_node(self, data):
        self.left_node = BinarySearchTree(data)
        return self.left_node

    def add_right_node(self, data):
        self.right_node = BinarySearchTree(data)
        return self.right_node

    def add_node(self, data):
        if data > self.data:
            if self.right_node == None:
                self.add_right_node(data)
            else:
                self.right_node.add_node(data)
        else:
            if self.left_node == None:
                self.add_left_node(data)
            else:
                self.left_node.add_node(data)


def main():
    root = BinarySearchTree(4)
    numbers = [6, 3, 9, 2, 4, 1, 2, 3, 9]

    for number in numbers:
        root.add_node(number)
    root.print_inorder()
    print()
    root.print_preorder()
    print()
    root.print_postorder()
    print()


if __name__ == "__main__":
    main()
