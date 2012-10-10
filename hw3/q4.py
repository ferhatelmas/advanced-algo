import itertools
import math

def find_max(l):
  i, skip, m = 0, int(len(l)/math.e), -1
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

# change me
n = 10

cnt = 0.0
for l in itertools.permutations(range(1, n+1)):
  if find_max(l) == n:
    cnt += 1
print cnt / fact(n)