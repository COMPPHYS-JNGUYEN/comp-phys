from scipy.interpolate import interp2d
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import transform, data, io

def interpol_im(im, dim1=8, dim2=8, plot_new_im=False, cmap='binary', axis_off=False):
    im = im[:,:,0]
    x = np.arange(im.shape[1])
    y = np.arange(im.shape[0])
    print(x.shape,y.shape)
    f2d = interp2d(x, y, im)
    
    x_new = np.linspace(0, im.shape[1], dim1)
    y_new = np.linspace(0, im.shape[0], dim2)
    
    im_new = f2d(x_new, y_new)
    
    im_flat = im_new.flatten()
    
    if plot_new_im:
        plt.imshow(im_new, cmap=cmap, interpolation='nearest')
        plt.grid('off')
        plt.show()
        
    return im_flat

def pca_X(X, n_comp=10):
    md_pca = PCA(n_comp)
    X_proj = pca.fit_transform(X)
    return md_pca, X_proj

def rescale_pixel(X, unseen, ind=0):
    dig_data = load_digits()
    X[ind] = dig_data.data
    
    return
    
def svm_train(X, y, gamma=0.001, C=100):
    
    return

def pca_svm_pred(imfile, md_pca, md_clf, dim1=45, dim2=60):
    im = mpimg.imread(imfile)
    f2d_flat = interpol_im(im, dim1=dim1, dim2=dim2)
    return

# letterB = mpimg.imread('letterB.png')
# letterB = letterB[:,:,0]


# dig_data = load_digits()
# X = dig_data.data
# y = dig_data.target

# print(letterB.shape)
# f2d = interpol_im(letterB, plot_new_im=True)
# # print(np.mean(X[0]), np.mean(letterB))