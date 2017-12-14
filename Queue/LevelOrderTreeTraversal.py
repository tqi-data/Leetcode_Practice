'''
Breadth-First Traversal of Binary Tree in Python. Given a binary tree, prints all it's elements level-by-level

           9
       2        4
    1    3   5     7
  
  output would be ->

  9
  2 4
  1 3 5 7

https://www.youtube.com/watch?v=NjdOhYKjFrU
'''


# using collections.deque allows fast appends and pops from both ends
from collections import deque

class Node:

       def __init__(self, val):
           self.val = val
           self.left = None
           self.right = None
           self.level = None

       def __str__(self):
           return str(self.val)

# BFT means breadth-first
def BFT(node):

    # current node level is 1
    node.level = 1
    current_level = node.level

    # put the first node into the queue
    queue = deque([node])
    output = []

    while len(queue)>0:
          # the first to arrive now leaves, using quque.popleft()
          current_node = queue.popleft()

          if(current_node.level > current_level):
              output.append("\n")
              current_level += 1

          output.append(str(current_node))

          if current_node.left != None:
             current_node.left.level = current_level + 1 
             queue.append(current_node.left) 

          if current_node.right != None:
             current_node.right.level = current_level + 1 
             queue.append(current_node.right)

                 
 
    return ''.join(output)

root = Node(9)
root.left = Node(2)
root.right = Node(4)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(5)
root.right.right = Node(7)

print BFT(root)
     
