# Python program to find out if two linked lists have a node in common (i.e., node that has the same value)

 
# Node class for linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
 
def solution(A, B):
    # Traverse the first linked list and store value of the nodes in dictionary
    d = {}
    while A:
        d[A.val] = 1
        A = A.next

    print d

    # Traverse the second linked list and search if the node is in the dictionary
    while B:
        if B.val in d:
             return True
        B = B.next

    return False

root1 = Node(4)
root1.next = Node (5)
root1.next.next = Node(6)
root1.next.next.next = Node(8)

root2 = Node(7)
root2.next = Node(8)
root2.next.next = Node(9)

Ans = solution(root1, root2)

if Ans:
    print 'There are common nodes.'
else:
    print 'There are no common nodes.'
