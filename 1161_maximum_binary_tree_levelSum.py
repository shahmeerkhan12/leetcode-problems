def bfs(root):
   q = []
   result = []
   
   if root is None:
      return []
   
   q.append(root)
   current_level = 0

   while q:
      q_len = len(q)
      result.append([])
      for _ in range(q_len):
         current_node = q.pop(0)
         result[current_level].append(current_node.data)
         if current_node.left is not None:
            q.append(current_node.left)
         if current_node.right is not None:
            q.append(current_node.right)
         
      current_level += 1
   level_sum = list(sum(row) for row in result)

   return level_sum.index(max(level_sum))+1

class Node:
   def __init__(self,value):
      self.data = value
      self.left = None
      self.right = None
root = Node(1)
n1 = Node(2)
n2 = Node(3) 
n3 = Node(4) 
n4 = Node(5) 
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

print(bfs(root))