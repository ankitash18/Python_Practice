class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None


def deletenode(node):
    node.value = node.nextnode.value
    node.nextnode = node.nextnode.nextnode

#testing

