import random
import math


def make_tree(a):
	num = len(a)
	level = int(math.ceil(math.log(num, 2)))
	t = [float("inf")]*(2**(level+1)-1)
	
	# childa < childb -> True
	# childa >= childb -> False
	t_cmp = [False]*(2**level-1)
	
	# init
	base = 2**level-1
	for i in xrange(0, num):
		t[base+i] = a[i]
#	print t
		
	# get minimum
	for l in xrange(level-1, -1, -1):
		level_size = 2**l
		base = 2**l-1
		for i in xrange(0, level_size):
			cur = base+i
			childa = cur*2+1
			childb = cur*2+2
#			print cur, childa, childb
			if t[childa] < t[childb]:
				t[cur] = t[childa]
				t_cmp[cur] = True
			else:
				t[cur] = t[childb]
	return t, t_cmp

def get_min(tree):
	return tree[0]
	
def get_sub_min(tree, tree_cmp):
	sub_min = 0
	child = 1
	if tree_cmp[0]:
		sub_min = tree[2]
		child = 1
	else:
		sub_min = tree[1]
		child = 2
		
	level = int(math.log(len(tree_cmp) + 1))
	for i in xrange(1, level):
		if tree_cmp[child]:
			val_child = tree[child*2 + 2]
			child = child*2 + 1
		else:
			val_child = tree[child*2 + 1]
			child = child*2 + 2
		if val_child < sub_min:
			sub_min = val_child
	return sub_min
	
LEN = 16

a = []
for i in xrange(LEN):
	a.append(random.randint(0,100))
	
print a
print math.log(2)
t, t_cmp = make_tree(a)
print t, t_cmp
print get_min(t)
print get_sub_min(t, t_cmp)
