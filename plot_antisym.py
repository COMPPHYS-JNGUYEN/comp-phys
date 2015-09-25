"""
#HW03
#James Nguyen
#Partner: Wenyi Gao

In quantum mechanics, if you place two identical fermions (e.g, electrons or neutrons) in an 
infinite square well between (0, a), you can solve for the individual wave function for each of these two particles.
However given that the total wave function of these two fermions should be antisymmetric, if
both have spin up (the spin part of their total wave function then is symmetric: you can switch
one particle for another and the total spin function is the same), then the total spatial wave
function should be antisymmetric. Suppose fermion 1 is in a state with a spatial quantum
number n1 and fermion 2 is in a state with a spatial quantum number n2, then the total wave
function should be: 

psi = (2./a)*(np.sin((n1*np.pi*x1)/a)*np.sin((n2*np.pi*x2)/a) - np.sin((n1*np.pi*x2)/a)*np.sin((n2*np.pi*x1)/a))

In quantum mechanics, |psi|^2 is the probability density. In this case, |psi(x1, x2)|^2dx1dx2 is the
probability of finding one particle in a small neighborhood around x1 and the other around x2.
Thus if |psi(x1, x2)|^2 is low, then it is very unlikely that one would find one particle around x1 and
the other around x2.

The program takes two positional arguments, x1 and x2, and three keyword arguments, n1, n2, and a, from the command line
and returns the wave function.  The wave function is then used to calculate the probability density.  The program
then plots the wave function and probability density side-by-side.



"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import argparse

def antisym(x1, x2, n1=1, n2=2, a=1.0):
    psi = (2./a)*(np.sin((n1*np.pi*x1)/a)*np.sin((n2*np.pi*x2)/a) - np.sin((n1*np.pi*x2)/a)*np.sin((n2*np.pi*x1)/a))
    return psi

if __name__ == "__main__":

    import doctest

    
    x01 = np.linspace(-1, 1, 50)
    x02 = np.linspace(-1, 1, 100)
    x001, x002 = np.meshgrid(x01, x02)
    wavefunction = antisym(x001, x002)
    prob_density = wavefunction**2


    fig = plt.figure()
    plt.suptitle('Antisymmetric Spatial Wave Function')

    psi = plt.subplot(121, projection = '3d')
    psi.plot_surface(x001, x002, wavefunction, rstride = 1, cstride = 1, cmap='Spectral', linewidth=.05)
    plt.title('Wave function')
    
    psisquared = plt.subplot(122, projection = '3d')
    psisquared.plot_surface(x001, x002, prob_density, rstride = 1, cstride = 1, cmap=cm.coolwarm, linewidth = .05)
    plt.title('Probability Density')
    
    txt = 'The "effective" interaction between two neutral Fermions (bothspin up) \nthat arises from the symmetry requirement \non the total wave function.'
    fig.text( .1, 0,txt)

    plt.show()