import math

def gamma_if_int(t):
    return math.factorial(t-1)

def f(x, t):
    return (x**(t-1))*(math.exp(-x))

def fractionaldifference(prev, curr):       
    frac_diff = (curr - prev)/float(curr)
    return frac_diff

def gamma_otherwise(t):     
    initial = 0
    final = 1000
    frac_diff = 1.
    dx = 1.
    integral_previous = 0.
    steps = (final - initial)/dx
    while frac_diff > 1e-4:
        integral_current = 0.
        for j in range(1, int(steps) + 1):
            height = f(initial + j*dx, t)
            area = dx*height
            integral_current += area
        frac_diff = fractionaldifference(integral_previous, integral_current)
        integral_previous = integral_current
        steps *= 2.
        dx /= 2.
    return integral_previous
def computegamma(t):
    if t < 1. or t > 100.:
        return "Please enter value that is between 1 and 100, inclusive."
    elif t == type(int):
        return gamma_if_int(t)
    else:
        return gamma_otherwise(t)


tee = input("Please input numerical value: ")
estimated_answer = computegamma(tee)
print estimated_answer