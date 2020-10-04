class BinaryTree:
    def __init__(self, data=None, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


def treeConstruction(preorder, inorder, inorder_start, inorder_end):

    if inorder_start > inorder_end:
        return None

    node = BinaryTree(preorder[treeConstruction.index_post])
    treeConstruction.index_post -= 1


    if inorder_start == inorder_end:
        return node

    inorder_index = search(inorder, inorder_start, inorder_end, node.data)
    node.right_node = treeConstruction(
        preorder, inorder, inorder_index + 1, inorder_end
    )
    node.left_node = treeConstruction(
        preorder, inorder, inorder_start, inorder_index - 1
    )
    return node

def search(array, start, end, info):
    for item in range(start, end + 1):
        if info == array[item]:
            return item

def printInorder(node):
    if node == None:
        return
    printInorder(node.left_node)
    print(node.data,end=" ")
    printInorder(node.right_node)       

def main():

    postorder = list(map(str, input("enter postorder").split()))
    inorder = list(map(str, input("enter inorder").split()))

    treeConstruction.index_post=len(postorder)-1
    root = treeConstruction(postorder, inorder, 0, len(inorder) - 1)

    print("INORDER TRAVERSAL")
    printInorder(root)


if __name__ == "__main__":
    main()
