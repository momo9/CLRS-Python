def quick_sort(a, p, r):
	if r-p > 1:
		q = get_pivot(a, p, r)
#		print p, q, r
#		raw_input("> ")
		quick_sort(a, p, q)
		quick_sort(a, q, r)
		
def get_pivot(a, p, r):
	
	pivot = a[r-1]
	
	i = p - 1
	for j in xrange(p, r-1):
		if a[j] <= pivot:			
			i += 1
			a[j], a[i] = a[i], a[j]
			
	a[r-1], a[i+1] = a[i+1], a[r-1]
	
	return i+1
	
a = [3, 7, 1, 23, 5, 2, 6]
quick_sort(a, 0, len(a))
print a
