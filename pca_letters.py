from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

from skimage import transform, data, io

# The key import of this cell:
from scipy.interpolate import interp2d

B = mpimg.imread('letterB.png')
print(B.shape)

ylo, yhi, xlo, xhi = 70, 220, 10, 200

B = B[ylo:yhi, xlo:xhi, 0]
B[0:150, 130:140] = 1

plt.imshow(B, cmap='gray')
plt.grid('off')
plt.show()