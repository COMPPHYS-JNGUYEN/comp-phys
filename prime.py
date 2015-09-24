"""
#HW03
#James Nguyen
#Partner: Howard Gao

This program finds the prime numbers from a desired range of numbers.  Given a starting number and ending number, prime.py will find all the prime numbers between and including the given numbers.

"""

import numpy as np

def find_primenumber(start, end):
    if start <= 1:
        start = 2
    arr = np.arange(start, end+1)
    prime = []
    for k in arr:
        j = 0
        for a in range(1, end+1):
            if k % a == 0:
                j += 1
        if j <= 2:
            prime.append(k)
    return prime
            
x = find_primenumber(1, 1000)
print x
print len(x)