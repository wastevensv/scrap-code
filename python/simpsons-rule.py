from __future__ import print_function
from math import *

try:
  input = raw_input
except NameError:
  pass

# f is hardcoded. Anyone know a good equation parsing library?
def f(x):
  return 1/sqrt(1-(x**2))

print("f(x)=1/sqrt(1-(x**2))")
# Obtain starting variables
a = float(input("a="))
b = float(input("b="))
n = int(input("n="))
if n%2: raise Exception("n must be even.")

# Calculate delta x.
deltax = (b-a)/n

# Start with outer points.
accum = f(a) + f(b)
#print('{0:.3f}, {1:d}*{2:.3f}={2:.3f}'.format(a,1,f(a)))

# Calculate inner points
for i in range(1,n):
  xi = a+(deltax*i)
  yi = f(xi)
  c= ((i%2)+1)*2
  t = c*yi
#  print('{0:.3f}, {1:d}*{2:.3f}={3:.3f}'.format(xi,c,yi,t))
  accum += t

#print('{0:.3f}, {1:d}*{2:.3f}={2:.3f}'.format(b,1,f(b)))

accum *= deltax/3
print("Ap: {0:.6f}".format(accum))
