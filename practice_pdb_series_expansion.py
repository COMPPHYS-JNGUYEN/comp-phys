import pdb
from math import log  #you would guess math module would have log...yes!
from math import log1p  #more accurate for small x.


def L(x, n):
    approx = 0.
    approx_prev = 0.
    if x <= -1:
        print "Cannot use given value"
        return
    for i in range(0, n+1):
        approx_prev = approx
        approx += (1/(i+1.))*(x/(1.+x))**(i+1.)
    if (approx - approx_prev)/approx > 10**(-6):
        print "Returned value is not within desried error.  Increase n."
        return approx
    else:
        return approx


x = 2
y = L(x, 100)
print 'Taylor Series Approximation:', y
exact_val = log(1+x)
print 'exact_val', exact_val
print 'log1p output', log1p(x)