`# Problem 4.1:
def route(graph, node1, node2):
  # graph = {1: [3,4,5], 2: [3,4]} --> False
  # graph = {1:[3,4,5],2:[4],3:[1,2]} --> True
  visited = set()
  queue = [node1]
  while queue:
    print(queue)
    curr = queue[0]
    if curr == node2: return True
    queue = queue[1:]
    if curr not in graph: continue
    for node in graph[curr]:
      if node in visited: continue
      queue.append(node)
    visited.add(curr)
  return False

graph = {1:[3,4,5],2:[4],3:[1,2]}
print(route(graph, 1,2))

# Problem 4.2:
class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    return

  def minimal_tree(self,asc_arr):
    if len(asc_arr) == 0: return None
    mid = int(len(asc_arr)/2)
    root = Node(asc_arr[mid])
    root.left = self.minimal_tree(asc_arr[:mid])
    root.right = self.minimal_tree(asc_arr[mid+1:])
    return root

  def bst_traversal(self,root):
    if root.val == None: return []
    curr = root
    curr_idx = 0
    queue = [root]
    while curr.left or curr.right:
      if curr.left: queue.append(curr.left)
      if curr.right: queue.append(curr.right)
      curr_idx += 1
      curr = queue[curr_idx]
    order = []
    for node in queue:
      order.append(node.val)
    return order

# Problem 4.3:
  def depth(self,root):
    if root.val == None: return []
    queue = [root]
    new_root = Node(root.val)
    all_levels = [new_root]
    next_level = []
    head = Node(None)
    temp = head
    while queue:
      curr = queue[0]
      queue = queue[1:]
      if curr.left: next_level.append(curr.left)
      if curr.right: next_level.append(curr.right)
      if not queue:
        queue = next_level
        next_level = []
        for node in queue:
          new_node = Node(node.val)
          temp.next = new_node
          temp = new_node
        all_levels.append(head.next)
        temp = head
    return all_levels

tree = Tree()
root = tree.minimal_tree([1,2,3,4,7,9])
print(tree.bst_traversal(root))


def find_next(node):
  if not node: return None
  if node.right: return node.right
  elif node.parent.left == node: return node.parent
  else:
    q = node.parent
    while q.parent.left != q:
      q = q.parent
    return q.parent
  return None
print(root.right.left.val)
print(find_next(root.right.left).val)

# Problem 4.5:
def is_bst(root, max_val, min_val):
  if not root: return True
  if (max_val and root.val > max_val ) or (min_val and root.val <= min_val):
    return False
  if (not is_bst(root.left, root.val, min_val )) or (not is_bst(root.right, max_val, root.val)):
    return False
  return True

print(is_bst(root, None, None))

# Problem 4.6:
def find_next(node):
  if not node: return None
  if node.right: return node.right
  elif node.parent.left == node: return node.parent
  else:
    q = node.parent
    while q.parent.left != q:
      q = q.parent
    return q.parent
  return None


  # Make and use a trie as a dictionary

  def make_trie(words):
  dictionary = collections.defaultdict(dict)
  for word in words:
    curr_dict = dictionary
    for letter in word:
      if letter not in curr_dict: curr_dict[letter] = {}
      curr_dict = curr_dict[letter]
    curr_dict["end"] = "end"
  return dictionary
    

words = ["foo", "bar", "barz", "cat"]

word_dict = make_trie(words)

def in_trie(trie, word):
  curr_dict = trie
  for letter in word:
    if letter not in curr_dict: return False
    curr_dict = curr_dict[letter]
  if "end" in curr_dict: return True
  return False

print(in_trie(word_dict, "cat"))


import collections
class Graph:
  def __init__(self, vertices):
    self.graph = collections.defaultdict(list)
    self.num_vertices = vertices # num of vertices with vertices 0 to vertices-1

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def topologicalSortUtil(self, v, visited,stack):
    visited[v] = True
    for connection in self.graph[v]:
      if visited[connection] == False:
        self.topologicalSortUtil(connection,visited, stack)
    stack.insert(0,v)

  def topologicalSort(self):
    visited = [False]*self.num_vertices
    stack = []

    for i in range(self.num_vertices):
      if visited == False:
        self.topologicalSortUtil(i, visited, stack)
    return stack

g = Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)


# Leetcode problem 103
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
  def zigzagLevelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    
    res = []
    
    r2l = False
    
    queue = deque([root])
    
    while queue:
      size = len(queue)
      currLevel = []
      for i in range(size):
        if r2l:
          curr = queue.pop()
          currLevel.append(curr.val)
          if curr.right: queue.appendleft(curr.right)
          if curr.left: queue.appendleft(curr.left) 
        else:
          curr = queue.popleft()
          currLevel.append(curr.val)
          if curr.left: queue.append(curr.left)
          if curr.right: queue.append(curr.right)
      res.append(currLevel)
      r2l = not r2l
    return res


# Leetcode: 684 Redundant Connection (medium)
# Implementing Union Find
# parent initialized as (x -> x)
class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0] * 1001

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        return True

class Solution(object):
    def findRedundantConnection(self, edges):
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge