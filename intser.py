#An example Python implementation of my serialization algorithm
#This file is public domain
#--Nikita Sadkov

def path12(n):
  if n == 0: return "e"
  if n == 1: return "0"
  if n&1: return "%s01" % path12(n/2)
  else: return "%s0" % path12(n/2)

#codes likes 1111, 11111,... are free
def enc12(n):
  n += 2
  r = 3 #termination code
  while n>1:
    if n&1: r = (r<<2)|2
    else: r <<= 1
    n >>= 1
  return r>>1

def dec12(n):
  r = 2
  while n&3 != 3 or n&7 == 7:
    if n&1: r |= 1
    else: r <<= 1
    n = n >> 1
  return r - 2

#these alt-versions use larger number of bits
def enc12a(n):
  n += 1
  r = 3 #termination code
  while n>0:
    if n&1: r = (r<<2)|1
    else: r <<= 1
    n >>= 1
  return r>>2

def dec12a(n):
  r = 0
  n = (n<<2)|1
  while n&3 != 3:
    r <<= 1
    if n&1:
      r |= 1
      n >>= 1
    n >>= 1
  return r-1

#using 2bit packing wastes even more bits for smaller numbers
def enc4(n):
  r = 7 #termination code
  while n>0:
    if n&3==3: r = (r<<3)|3
    else: r = (r<<2)|(n&3)
    n >>= 2
  return r

def dec4(n):
  r = 0
  while n and (n&7 != 7):
    r <<= 2
    if n&7 == 3:
      r |= 3
      n >>= 1
    else:
      r |= (n&3)
    n >>= 2
  return r

for n in range(0,256):
  p = "{0:b}".format(enc4(n))[::-1]
  print("%3d->%4d:%2d,%s" %
        (n,dec4(enc4(n)),len(p),p))
