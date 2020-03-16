class Deque(object):

    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self,item):
        self.items.append(item)

    def addread(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRead(self):
        return self.items.pop(0)

d = Deque()

print(d.isEmpty())

d.addFront('hello')

d.addread('world')

print(d.removeFront()+ ' ' + d.removeRead())

print(d.size())