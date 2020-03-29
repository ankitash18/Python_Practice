#create node

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None


a = Node(1)

b= Node(2)

c = Node(3)

a.nextnode = b

b.nextnode =c

print(a.value)

print(a.nextnode.value)

def deletenode(node):
    node.value = node.nextnode.value
    node.nextnode = node.nextnode.nextnode

d = deletenode(Node(2))

