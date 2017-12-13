# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [[root, root]]
        
        while queue:
            # pairs always get the first element of the queue 
            pairs = queue.pop(0)
            a = pairs[0]
            b = pairs[1]
            
            if not a and not b:
                continue
            elif a and b and a.val == b.val:
                queue.append([a.left, b.right])
                queue.append([a.right, b.left])
            else:
                return False
        
        return True

# Driver program to test
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)


a = Solution()
Ans1 = a.isSymmetric(root1)
Ans2 = a.isSymmetric(root2)

if Ans1: 
   print "Tree 1 is symmetric." 
else:
   print "Tree 1 is asymmetric."

if Ans2:
   print "Tree 2 is symmetric."
else:
   print "Tree 2 is asymmetric." 

