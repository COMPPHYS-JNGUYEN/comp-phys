'''
    
    Note: this is a series expansion, but a Taylor Series!
    The usual Taylor series for log(1+x) has a converge range of -1<x<=1
    This is based on ln(x) = sum( (1/n) ((x-1)/x)^n ) -- replacing x by x + 1,
    we get the formula below.
    
    The advantage is now the convergence radius is x > -1
    
    We will improve this function further by adding a doctest.
    
    
    
    >>> L(1) - 0.69314718056 < 1e-6
    True

    Call signature  :
    
    python Doctest_argparse_example.py -x 2. 
    
    To run doctests in verbose mode:
    
    python -m doctest -v Doctest_argparse_example.py

'''

def L(x, n = 1000):
    if x <= -1:
        print 'Error: x cannot be < -1.  Returning...'
        return
    approx = 0
    approx_prev = 0
    for i in range(1, n):
        approx += (1./i)*(x/(1.+x))**i
        if i == n-2:
            approx_prev = approx
    frac_diff = (approx - approx_prev)/approx
    if frac_diff > 1e-6:
        print 'Please increase the value of n for higher accuracy...'
        print 'frac_diff:', frac_diff
        return approx
    
    return approx

if __name__ == "__main__":

    import doctest
    import argparse
    from math import log, log1p



    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type = float)
    args = parser.parse_args()
    x = args.x

#   x = 1000
    y = L(x)
    print 'Series Approximation:', y
    from math import log  #you would guess math module would have log...yes!
    exact_val = log(1+x)
    print 'exact_val', exact_val
    print 'log1p output', log1p(x)