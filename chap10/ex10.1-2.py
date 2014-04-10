class TWO_STACKS:
  
  def __init__(self, size):
    self.container = [0] * size
    self.topa = 0
    self.topb = size - 1
    #print "init"
    #print self.container

  def pusha(self, num):
    if self.topb < self.topa:
      print "Stack A upflowed!"
      return
    else:
      self.container[self.topa] = num
      self.topa += 1
      print "Push %d to A" % num

  def popa(self):
    if self.topa == 0:
      print "Stack A downflowed!"
    else:
      self.topa -= 1
      return self.container[self.topa]

  def pushb(self, num):
    if self.topb < self.topa:
      print "Stack B upflowed!"
      return
    else:
      self.container[self.topb] = num
      self.topb -= 1
      print "Push %d to A" % num

  def popb(self):
    if self.topb == len(self.container) - 1:
      print "Stack B downflowed!"
    else:
      self.topb += 1
      return self.container[self.topb]

  def print_info(self):
    print self.container
    print "topa:", self.topa, "topb", self.topb
    print

stack = TWO_STACKS(4)
stack.print_info()

stack.pusha(10)
stack.print_info()
stack.pusha(11)
stack.print_info()
stack.pushb(1)
stack.print_info()
stack.pusha(3)
stack.print_info()
stack.pusha(5)
stack.print_info()
stack.pushb(6)
stack.print_info()

print stack.popa()
stack.print_info()
print stack.popb()
stack.print_info()
print stack.popb()
stack.print_info()

