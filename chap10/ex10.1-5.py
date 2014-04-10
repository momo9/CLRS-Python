# CLRS excercise 10.1-5
# deque implemented with array

class Deque:
  def __init__(self, n):
    self.cntnr = [0] * n
    self.head = 0
    self.tail = 0
    self.cpcty = n

  def printQueue(self):
    print "head: %d, tail: %d, queue:" % (self.head, self.tail),
    if self.head <= self.tail:
      for i in xrange(self.head, self.tail):
        print self.cntnr[i],
      print
    else:
      for i in xrange(self.head, self.cpcty):
        print self.cntnr[i],
      for i in xrange(0, self.tail):
        print self.cntnr[i],
      print

  def pushBack(self, n):
    print "push %d to back" % n
    if self.tail == self.head - 1 or self.tail - self.head == self.cpcty - 1:
      print "Upflow"
    else:
      self.cntnr[self.tail] = n
      if self.tail == self.cpcty - 1:
        self.tail = 0
      else:
        self.tail += 1
      self.printQueue()

  def popFront(self):
    print "pop front"
    if self.tail != self.head:
      res = self.cntnr[self.head]
      if self.head == self.cpcty - 1:
        self.head = 0
      else:
        self.head += 1
      self.printQueue()
      return res
    else:
      print "Downflow"
      return None

  def pushFront(self, n):
    print "push %d to front" % n
    if self.tail == self.head - 1 or self.tail - self.head == self.cpcty - 1:
      print "Upflow"
    else:
      if self.head == 0:
        self.head = self.cpcty - 1
      else:
        self.head -= 1
      self.cntnr[self.head] = n
    self.printQueue()
    
  def popBack(self):
    print "pop back"
    if self.tail == self.head:
      print "Downflow"
      return None
    else:
      if self.tail == 0:
        self.tail = self.cpcty - 1
      else:
        self.tail -= 1
      res = self.cntnr[self.tail]
      self.printQueue()
      return res

q = Deque(5)
q.pushBack(1)
print q.popFront()
print q.popBack()
q.pushFront(2)
q.pushBack(3)
q.pushBack(4)
q.pushFront(5)
q.pushBack(6)
print q.popFront()
q.pushBack(7)
q.pushBack(8)
print q.popFront()
print q.popBack()
print q.popBack()
print q.popFront()
print q.popFront()
print q.popFront()
q.pushBack(9)

