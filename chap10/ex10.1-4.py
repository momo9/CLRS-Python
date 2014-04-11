# CLRS exercise 10.1-4
# enqueue() & dequeue() that can deal with overflow

class Queue:
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

  def enqueue(self, n):
    if self.tail == self.head - 1:
      print "Upflow"
    else:
      self.cntnr[self.tail] = n
      if self.tail == self.cpcty - 1:
        self.tail = 0
      else:
        self.tail += 1
      q.printQueue()

  def dequeue(self):
    if self.tail != self.head:
      res = self.cntnr[self.head]
      if self.head == self.cpcty - 1:
        self.head = 0
      else:
        self.head += 1
      q.printQueue()
      return res
    else:
      print "Downflow"
      return None

q = Queue(4)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
q.enqueue(5)
q.enqueue(5)
q.enqueue(13)
q.enqueue(2)
print q.dequeue()
q.enqueue(4)
q.enqueue(6)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
q.enqueue(8)

