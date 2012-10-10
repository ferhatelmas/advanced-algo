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

# change me
l = range(1, 10)

cnt = 0
for l in itertools.permutations(range(1, 11)):
  if find_max(l) == 10:
    cnt += 1

print cnt / 3628800.0