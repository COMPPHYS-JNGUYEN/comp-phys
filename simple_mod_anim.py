"""
A simple example of an animated plot.  

Modified based on the following sources:

https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/
http://matplotlib.org/examples/animation/simple_anim.html
    
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ipdb import set_trace

fig, ax = plt.subplots()

# creating an empty line object
line, = ax.plot([], [], lw=2)

ax.set_xlim([0, 2*np.pi])
ax.set_ylim([-2, 2])

# initialization function:
# Create the functions which make the animation happen.  init() is the function which will be called to create the base frame upon which the animation takes place. This is a simple function which sets the line data to nothing. It is important that this function return the line object, because this tells the animator which objects on the plot to update after each frame:

def init():
    line.set_data([], [])
    return line,


#The animation function. It takes a single parameter, the frame number i, and draws the function with a shift that depends on i, and then updates the object line.
def animate(i):
    t_ani = t + i/10.0
    x = np.sin(t_ani)*np.exp(-t_ani*0.05)
    line.set_data(t, x)  # update the data
    return line,


# We've chosen a 500 frame animation with a 25ms delay between frames.
# The blit keyword tells the animation to only re-draw the pieces of the plot which have changed. The time saved with blit=True means that the animations display much more quickly.

t = np.arange(0, 100*np.pi, 0.001)

# Note how convenient it is to treat everything as objects so that they can be passed
# to a function (another object): fig, animate, init.
ani = animation.FuncAnimation(fig, animate, frames = 500, init_func=init,
                              interval=25, blit=True)
plt.show()
