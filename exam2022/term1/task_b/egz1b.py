from egz1btesty import runtests
from queue import PriorityQueue

class Node:
  def __init__(self):
    self.left = None    # left subtree
    self.right = None   # right subtree
    self.level = None   # level
    self.childs = 0

def wideentall(T: Node):
  q = []
  levels = []
  nodes = []
  T.level = 0
  q.append(T)
  while len(q) > 0:
    node = q.pop(min(enumerate(q), key=lambda x: x[1].level)[0])
    nodes.append(node)

    if len(levels) - 1 < node.level:
      levels.append([])
    
    levels[node.level]

    if node.left:
      node.childs +=1
      node.left.level = node.level + 1
      q.append(node.left)
    if node.right:
      node.childs +=1
      node.right.level = node.level + 1
      q.append(node.right)

  to_cut = 0
  for i in range(1, len(levels)):
    if levels[i + 1] < levels[i]:
      to_cut += levels[i + 1]
  
  

  return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests( wideentall, all_tests = False )