import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ipdb import set_trace
from scipy.integrate import odeint

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

# creating an empty line object
line, = ax.plot([], [], 's-', lw=2)

ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

y0, t0 = [np.pi/2, 0], 0

def HO(y, t, b, c):
    '''
        Harmonic oscillator
        
        b: drag coeff
        c: k/m
        
        x --> Theta
        v --> Omega
        '''
    x, v = y[0], y[1]
    dxdt, dvdt = v, -b*v - c*np.sin(x)
    return [dxdt, dvdt]

t1 = np.pi*4
dt = 0.01
t_arr = np.arange(0, t1, dt)

b = 0.001
g = 9.8
l = 10
c = g/l

th_o = odeint(HO, y0, t_arr, args=(b, c))
th = th_o[:, 0]
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
#o = th_o[:, 1]

def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    #t_ani = t + i/10.0
#    curr_t = t_arr[i]
    curr_theta = th[i]
#    curr_o = o[i]
    
    curr_x = l*np.sin(curr_theta)
    curr_y = l*np.cos(curr_theta)
    
    #dt = 0.01
    
    
    #line.set_data(t, x)  # update the data
    line.set_data([0,curr_x], [0,-curr_y])
    time_text.set_text(time_template % (i*dt))
    return line, time_text


# We've chosen a 500 frame animation with a 25ms delay between frames.
# The blit keyword tells the animation to only re-draw the pieces of the plot which have changed. The time saved with blit=True means that the animations display much more quickly.

# Note how convenient it is to treat everything as objects so that they can be passed
# to a function (another object): fig, animate, init.
ani = animation.FuncAnimation(fig, animate, frames = 1257, init_func=init,
                              interval=25, blit=True)

#plt.plot(t_arr, th)
#plt.plot(t_arr, o)
plt.show()