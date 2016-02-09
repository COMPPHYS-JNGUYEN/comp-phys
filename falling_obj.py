import numpy as np

def height(h0, v0, t):
    g = 9.8
    h = h0 + v0*t - .5*g*(t**2)
    if h <= 0.:
        return 0
    return h

def vel(h0, v0, t):
    g = 9.8
    v = v0 - g*t
    if height(h0, v0, t) <= 0:
        return 0
    return v

def test_height():
    assert height(10, 2, 1e6) == 0
def test_vel():
    assert vel(10, 2, 1e6) == 0