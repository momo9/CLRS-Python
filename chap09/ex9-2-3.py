import sys

def get_pivot(a, p, r):
	
	pivot = a[r-1]
	
	i = p - 1
	for j in xrange(p, r-1):
		if a[j] <= pivot:			
			i += 1
			a[j], a[i] = a[i], a[j]
			
	a[r-1], a[i+1] = a[i+1], a[r-1]
	
	return i+1

def order_static(a, i):
	i -= 1
	p = 0
	r = len(a)
	while True:
		q = get_pivot(a, p, r)
		if q == i:
			return a[q]
		if q < i: # in a[q+1 : ]
			p = q+1
		else:
			r = q
	
a = [3, 7, 1, 23, 5, 2, 6]
i = int(sys.argv[1])
print a
print order_static(a, i)