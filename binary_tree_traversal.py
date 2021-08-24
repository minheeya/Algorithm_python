#     (1)
#     /  \
#    (2)  (3)
#    / \   
#  (4) (5)

#Inorder (Left, Root, Right)  4 2 5 1 3
#Preorder (Root, Left, Right) 1 2 4 5 3
#Postorder (Left, Right, Root) 4 5 2 3 1

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def setRoot(self, node):   #root node 지정
        self.root = node

    def makeNode(self, left_node, data, right_node):
        node = Node(data)
        node.left = left_node
        node.right = right_node  
        return node

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.val, end = ' ')
            self.in_order(node.right)
        return
    
    def pre_order(self, node):
        if node:
            print(node.val, end = ' ')
            self.pre_order(node.left)
            self.pre_order(node.right)
        return
    
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val, end = ' ')
        return

if __name__ == '__main__':
    bt = BinaryTree()
    n4 = bt.makeNode(None, 4, None)
    n5 = bt.makeNode(None, 5, None)
    n2 = bt.makeNode(n4, 2, n5)
    n3 = bt.makeNode(None, 3, None)
    n1 = bt.makeNode(n2, 1, n3)
    bt.setRoot(n1)
    
    print('Inorder ', end = ' ')
    bt.in_order(bt.root)
    print('\nPreorder ', end = ' ')
    bt.pre_order(bt.root)
    print('\nPostorder ', end = '')
    bt.post_order(bt.root)