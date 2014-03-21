def get_mid(x, px, rx, y, py, ry):
	print px, rx, py, ry
	raw_input("> ")
	if rx - px <= 1 or ry - py <= 1: #all elements searched
		return min(x[px], y[py])
	else:
		mx = (px+rx) / 2; val_mx = x[mx]
		my = (py+ry) / 2; val_my = y[my]
		print "x[%d]: %d; y[%d]: %d" % (mx, val_mx, my, val_my)
		if val_mx == val_my: # must be the middle
			return val_mx
		else:
			if val_mx < val_my:
#				print "branch 1"
				if (rx-px) % 2 == 0: # when getting upper part of an even-length array, the partition scheme is different
					mx -= 1
				return get_mid(x, mx+1, rx, y, py, my)
			else:
#				print "branch 2"
				if (ry-py) % 2 == 0: # when getting upper part of an even-length array, the partition scheme is different
					my -= 1
				return get_mid(x, px, mx, y, my+1, ry)

x = [1, 30, 50, 70, 90]
y = [6, 8, 10, 12, 113]

print get_mid(x, 0, len(x), y, 0, len(y))
