# problem 7-6

class Ran(object):
	def __init__(self, lb, ub):
		self.lb = lb
		self.ub = ub
		
	def compare(self, rhs):
		if self.ub < rhs.lb:
			return -1
		elif self.lb > rhs.ub:
			return 1
		else:
			return 0
	
	def inter(self, rhs):
		if self.compare(rhs) == 0:
			lb = max(self.lb, rhs.lb)
			ub = min(self.ub, rhs.ub)
#			print lb, ub
			return Ran(lb, ub)
		else:
			return None

def quick_sort(a, p, r):
	if r-p > 1:
		q, t = get_pivot(a, p, r)
#		print p, q, r
#		raw_input("> ")
		quick_sort(a, p, q)
		quick_sort(a, t, r)
		
def get_pivot(a, p, r):
	
	pivot = a[r-1]
	
	i = p - 1
	k = p - 1
	for j in xrange(p, r-1):
		cmp = a[j].compare(pivot)
		if cmp == -1 or cmp == 0:			
			k += 1
			a[j], a[k] = a[k], a[j]
			if cmp == -1:
				i += 1
				a[i], a[k] = a[k], a[i]
			else:
				pivot = pivot.inter(a[k])
			
	a[r-1], a[k+1] = a[k+1], a[r-1]
	
	return i+1, k+2
	
a = [Ran(3,6), Ran(2,5), Ran(5, 7), Ran(4,8), Ran(0,5)]
#print get_pivot(a, 0, len(a))

quick_sort(a, 0, len(a))
for i in a:
	print i.lb, i.ub

