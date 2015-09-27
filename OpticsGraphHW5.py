from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


i = np.linspace(-2*np.pi, 2*np.pi, 100)
t = np.arcsin((1.33/1.000293)*np.sin(i))
plt.plot(i, t)
plt.xlabel('Incident Angle')
plt.ylabel('Transmitted Angle')
plt.title('Incident vs. Transmitted')
plt.show()