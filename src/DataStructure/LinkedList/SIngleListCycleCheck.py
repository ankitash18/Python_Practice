class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

def cycle_check(Node):

    marker1 = Node
    marker2 = Node

    while marker2 !=None    and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False

a = Node(1)

b = Node(2)

c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a#cyle here



#create non cycle list

x = Node(1)
y = Node(2)

z = Node(3)

x.nextnode = y
y.nextnode = z

ans = cycle_check(a)

ans1 = cycle_check(x)

print(ans)
print(ans1)

#using set

def hasCycle(self, head: Node) -> bool:
    seen = set()
    while head != None:
        if head in seen:
            return True
        else:
            seen.add(head)
            head = head.next
    return False


#reversal linked list

def reverse(head):
    #setup current ,previous and next nodes
    current = head
    previous = None
    nextnode =None

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode

    return  previous

#Nth to last node
#remove n th node from last node

def nth_to_last(n,head):
    left = head
    right = head

    for i in range(n):
        if not right.nextnode:
            raise LookupError('Error:n is larger then the linked list')

            right = right.nextnode

    while right.nextnode:
        left = left.nextnode
        right = right.nextnode

    return left


#other leetcode example
#merge two sorted linked list

def mergeTwoLists(self, l1, l2):
    # edge case check
    if not l1:
        return l2

    if not l2:
        return l1

    temp = dummyhead = Node(-1)

    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next

    if l1:
        temp.next = l1

    if l2:
        temp.next = l2

    return dummyhead.next


#palidrome inked list
#usingextra spaece

def isPalindrome(self, head):
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]

#The algorithm has two steps:

#Find the midpoint of the linked list
#Push the second half values into the stack
#Pop values out from the stack, and compare them to the first half of the linked list
#The advantages of this algorithm are we don't need to restore the linked list and the space complexity is acceptable (O(N/2))


def isPalindrome(self, head):
    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True