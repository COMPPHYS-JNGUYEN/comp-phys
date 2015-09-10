import pdb
from math import log  #you would guess math module would have log...yes!
from math import log1p  #more accurate for small x.


def L(x, n):
    approx = 0.
    #pdb.set_trace()
    if x <= -1:
        print "Cannot use given value"
        return
    else:
        for i in range(0, n+1):
            approx += (1/(i+1.))*(x/(1.+x))**(i+1.)
        return approx


x = 1
y = L(x, 100)
print 'Taylor Series Approximation:', y
exact_val = log(1+x)
print 'exact_val', exact_val
print 'log1p output', log1p(x)