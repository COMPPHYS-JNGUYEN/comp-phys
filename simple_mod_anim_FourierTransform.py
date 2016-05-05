import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ipdb import set_trace
from scipy.integrate import odeint

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

# creating an empty line object
line, = ax.plot([], [], 's-', lw=2)

ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

def DP(y, t, m, l, g):
    '''
        Double Pendulum
        
        b: drag coeff
        c: k/m
        
        x --> Theta
        v --> Omega
        '''
    theta1, w1, theta2, w2 = y[0], y[1], y[2], y[3]
    dtheta = theta1 - theta2
    theta1_dot = w1
    w1_dot = -.5*m*(l**2)*(w1*w2*np.sin(dtheta) + 3.*(g/l)*np.sin(theta1))
    theta2_dot = w2
    w2_dot = -.5*m*(l**2)*(-w1*w2*np.sin(dtheta) + (g/l)*np.sin(theta2))
    return [theta1_dot, w1_dot, theta2_dot, w2_dot]

y0, t0 = [np.pi/2, 0, np.pi/4, 0], 0

t1 = np.pi*4
dt = 0.01
t_arr = np.arange(0, t1, dt)

g = 9.8
l = 1
m = 1


DP_stuff = odeint(DP, y0, t_arr, args=(m, l, g))

theta1 = DP_stuff[:, 0]
w1 = DP_stuff[:, 1]
theta2 = DP_stuff[:, 2]
w2 = DP_stuff[:, 3]

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
    curr_theta1 = theta1[i]
    curr_theta2 = theta2[i]
#    curr_o = o[i]
    
    curr_x1 = np.sin(curr_theta1)
    curr_y1 = -np.cos(curr_theta1)
    curr_x2 = curr_x1 + np.sin(curr_theta2)
    curr_y2 = curr_y1 - np.cos(curr_theta2)
    
    #dt = 0.01
    
    
    #line.set_data(t, x)  # update the data
    line.set_data([0, curr_x1, curr_x2], [0, curr_y1, curr_y2])
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