import random

def pre_proc(a, k):

	length = len(a)
	c = [0]*k
	
	for i in xrange(0, k):
		c[i] = 0
		
	for i in xrange(0, length):
		c[a[i]] += 1
		
	for i in xrange(1, k):
		c[i] += c[i-1]
		
	return c
	
def get_num(c, a, b):
	if a == 0:
		return c[b]
	else:
		return c[b] - c[a-1]

def radix_sort(a, n):
	
	length = len(a)
	
	for r in xrange(0, 3):
		d = [0]*length
		for i in xrange(0, length):
			d[i] = a[i]/(n**r)%n
		c = pre_proc(d, n)
#		print d
#		print c
#		raw_input("> ")
		b = [0]*length
		for i in xrange(length-1, -1, -1):
			b[c[d[i]]-1] = a[i]
			c[d[i]] -= 1
		a = b
		
	return a

N = 10
		
LEN = 20
a = []

for i in xrange(0, LEN):
	r2 = random.randint(0, N-1)
	r1 = random.randint(0, N-1)
	r0 = random.randint(0, N-1)
	a.append((N**2)*r2 + N*r1 + r0)
	
print a
b = radix_sort(a, N)
print b

	

