class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if id(slow) == id(fast):
                return True
            
        return False


node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node4 = Node(26)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

a = Solution()
Ans = a.hasCycle(node1)

if Ans:
   print "There is a cycle."
else:
   print "There is not a cycle."

