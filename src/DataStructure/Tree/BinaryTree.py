class BinaryTree():
    def __init__(self,root):
        self.key = root
        self.leftchild = None
        self.rightchild = None

    def insertleft(self,newNode):
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)
        else:
            t= BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self,newNode):
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        return  self.rightchild

    def leftchild(self):
        return self.leftchild

    def setrootval(self,obj):
        self.key = obj

    def getrootval(self):
        return self.key




r = BinaryTree('a')

rootval = r.getrootval()

print(rootval)

r.insertleft('b')

#is BST

class Solution(object):
    def isValidBST(self, root):
        serialized = []
        self.inorder(root, serialized)
        for i in range(1, len(serialized)):
            if serialized[i-1] >= serialized[i]:
                return False
        return True

    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)



#print level orfd tresal

# Iterative Method to print the height of binary tree
def printLevelOrder(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

            # Enqueue right child
        if node.right is not None:
            queue.append(node.right)