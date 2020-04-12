"""

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


"""

class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    tempa = headA
    temb = headB
    lena = 0
    lenb = 0
    while tempa != None:
        lena += 1
        tempa = tempa.next
    while tempb != None:
        lenb += 1
        tempb = tempb.next

    tempa = headA
    tempb = headB
    if lena > lenb:
        diff = lena - lenb
        while diff != 0:
            tempa = tempa.next
            diff -= 1
    else:
        diff = lenb - lena
        while diff != 0:
            tempb = tempb.next
            diff -= 1
    while tempa != None and tempb != None:
        if tempa ==temb:
            return tempa
        tempa = tempa.next
        tempb = tempb.next

    return None
