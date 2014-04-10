# CLRS excercise 10.2-4
# Circular, doubly linked list with a sentinel
class CirDouList:
  def __init__(self):
    self.__nil = Node()

  def trav(self):
    l = self.__nil
    while not (l.post is self.__nil):
      l = l.post
      print l.val,
    print

  def insert(self, n, val): # n.post -> new -> n
    back = n.pre
    #back.printNode()
    node = Node(back, val, n)
    back.post = node
    n.pre = node
    self.trav()


  def insertBack(self, val):
    self.insert(self.__nil, val)

  def insertFront(self, val):
    self.insert(self.__nil.post, val)

  def printNil(self):
    self.__nil.printNode()

class Node:
  def __init__(self, *args):
    argv = len(args)
    if argv == 0: # a nil node
      pre = post = self
      val = 0
    elif argv == 3: # normal node
      pre, val, post = args
    self.pre = pre
    self.val = val
    self.post = post
  
  def printNode(self):
    print self.pre, self.val, self.post
    

l = CirDouList()
l.insertBack(5)
l.insertBack(6)
l.insertBack(7)
l.insertFront(8)
l.insertFront(9)

