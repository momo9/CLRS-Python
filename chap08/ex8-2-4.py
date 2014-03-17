import random

def pre_proc(a):

	length = len(a)
	c = [0]*length
	
	for i in xrange(0, length):
		c[i] = 0
		
	for i in xrange(0, length):
		c[a[i]] += 1
		
	for i in xrange(1, length):
		c[i] += c[i-1]
		
	return c
	
def get_num(c, a, b):
	if a == 0:
		return c[b]
	else:
		return c[b] - c[a-1]
	
LEN = 10
a = []

for i in xrange(0, LEN):
	a.append(random.randint(0, LEN-1))
	
print a
c = pre_proc(a)
print c
print get_num(c, 1, 9)
