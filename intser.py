#An example Python implementation of my serialization algorithm
#This file is public domain
#--Nikita Sadkov

def path12(n):
  if n == 0: return "e"
  if n == 1: return "0"
  if n&1: return "%s01" % path12(n/2)
  else: return "%s0" % path12(n/2)

def enc12p(p):
  n = 0
  r = 0
  for c in p:
    r |= int(c)<<n
    n += 1
  r += 3<<n
  return r

def enc12(n):
  n += 3
  r = 3 #termination code
  while n>1:
    if n&1: r = (r<<2)|2
    else: r = r<<1
    n >>= 1
  return r>>1

def dec12(n):
  r = 2
  while n&3 != 3 or n&7 == 7:
    if n&1: r ^= 1
    else: r <<= 1
    n = n >> 1
  return r - 3

for n in range(0,30):
  p = "%s11"%path12(n+3)[2:]
  print("%3d->%4d:%2d,%2d,%2d,%s" %
        (n,enc12(n),len(p),p.count('1'),p.count('0')
        ,"{0:b}".format(enc12(n))[::-1]))
