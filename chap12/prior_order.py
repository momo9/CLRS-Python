# prior order traversal of binary tree
def prior_order_trav(t, n):

  length = len(t)
  print t[n]

  left = get_left(n)
  if left < length:
    prior_order_trav(t, left)
  else:
    return

  right = get_right(n)
  if right < length:
    prior_order_trav(t, right)

def get_parent(n):
  return (n - 1) / 2

def get_left(n):
  return 2 * n + 1

def get_right(n):
  return 2 * n + 2

t = range(0, 10)
prior_order_trav(t, 0)
