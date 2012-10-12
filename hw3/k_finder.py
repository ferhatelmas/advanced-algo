s = 0
for n in xrange(2, int(raw_intput())+1):
  for i in xrange(2, n+1):
    for j in xrange(i, n+1):
      s += 1.0/(j-1)
    s *= ((i-1.0)/n)
    if s > 0.25:
      print n, "->", i
      break;