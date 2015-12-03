from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import transform, data, io
from scipy.interpolate import interp2d

##################################################

def make_let_im(let_file, dim=16, ylo=70, yhi=220, xlo=10, xhi=200, edge_pix=150, plot_let=False):
    letter = mpimg.imread(let_file)
    
    letter = letter[ylo:yhi, xlo:xhi, 0]
    letter[0:edge_pix, 130:140] = 1
    
    plt.imshow(letter, cmap='gray')
    plt.grid('off')
    plt.show()
    
    x = np.arange(letter.shape[1])
    y = np.arange(letter.shape[0])
    
    f2d = interp2d(x, y, letter)
    
    x_new = np.linspace(0, letter.shape[1], dim)
    y_new = np.linspace(0, letter.shape[0], dim)
    
    letter_new = f2d(x_new, y_new)
    
    letter_flat = letter_new.flatten()
    
    if plot_let:
        plt.imshow(letter_new, cmap = 'gray')
        plt.grid('off')
        plt.show()
    
    return letter_new, letter_flat

B = 'letterB.png'
let, let_flat = make_let_im(B)