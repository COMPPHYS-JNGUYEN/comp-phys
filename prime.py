"""
#HW03
#James Nguyen
#Partner: Howard Gao

This program finds the prime numbers from a desired range of numbers.  Given a starting number and ending number, prime.py will find all the prime numbers between and including the given numbers.


>>> find_primenumber(-2, 100)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

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
            

if __name__ == "__main__":

    import doctest
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', type = int)
    parser.add_argument('-f', type = int)
    args = parser.parse_args()
    begin = args.b
    finish = args.f
    x = find_primenumber(begin, finish)
    print x
    