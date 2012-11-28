from itertools import permutations
from sys import argv

def find_k(n):
  total_prob = 0
  for k in xrange(2, n+1):
    for i in xrange(k, n+1):
      total_prob += 1.0/(i-1)
    total_prob *= ((k-1.0)/n)
    if total_prob > 0.25:
      return k

def find_max(l, skip):
  i, m = 0, -1
  for e in l:
    if i <= skip:
      m = max(m, e)
      i += 1
    else:
      if e > m:
        return e
  return l[-1]

def fact(n):
  if n <= 1:
    return n
  else:
    return n * fact(n-1)

n = int(argv[1])
cnt, k = 0.0, find_k(n)
for l in permutations(range(1, n+1)):
  if find_max(l, k) == n:
    cnt += 1
print "n: %d skip: %d prob: %.3f" % (n, k, cnt / fact(n))