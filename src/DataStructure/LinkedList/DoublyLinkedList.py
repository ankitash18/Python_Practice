class DoublyLinkedListNode(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.prevnode =None

a = DoublyLinkedListNode(1)

b = DoublyLinkedListNode(2)

c = DoublyLinkedListNode(3)

a.nextnode = b
b.prevnode = a
b.nextnode = c
c.prevnode = b
