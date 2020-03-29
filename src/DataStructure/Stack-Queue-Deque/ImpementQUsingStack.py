class Queue2Stack(object):

    def __init__(self):
        #two stacks
        self.instack =[]
        self.outstack =[]

    def enqueue(self,element):
        self.instack.append(element)

    def dequeu(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q2 = Queue2Stack()

