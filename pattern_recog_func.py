"""
File contains a library of python functions.  
interpol_im - interpolates an image and flattens it, returning the flattened image.  
pca_X - projects a dataset, X, onto pca space and returns md_pca and X_proj.  
rescale_pixel - rescales the unseen image according to the X dataset and returns the scaled unseen image.  
svm_train - trains the dataset X, making a classifier, and returns the classifier.
pca_svm_pred - takes an image file, reads it, interpolates it, projects the interpolated image onto pca space, then returns a prediction for the image.
"""

from scipy.interpolate import interp2d
from skimage import transform, data, io
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn import preprocessing
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pdb import set_trace


def interpol_im(im, dim1=8, dim2=8, plot_new_im=False, cmap='binary', axis_off=False):
    im = im[:,:,0]
    x = np.arange(im.shape[1])
    y = np.arange(im.shape[0])

    f2d = interp2d(x, y, im)
    
    x_new = np.linspace(0, im.shape[1], dim1)
    y_new = np.linspace(0, im.shape[0], dim2)
    im_new = -f2d(x_new, y_new)
    
    im_flat = im_new.flatten()
    
    if plot_new_im:
        plt.imshow(im_new, cmap=cmap, interpolation='nearest')
        if axis_off:
            plt.grid('off')
        plt.show()
        
    return im_flat

def pca_X(X, n_comp=10):
    md_pca = PCA(n_components=n_comp, whiten=True)
    X_proj = md_pca.fit_transform(X)
    return md_pca, X_proj

def rescale_pixel(X, unseen, ind=0):
    X_train = X[ind]
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(min(X_train), max(X_train)))
    unseen_scaled = min_max_scaler.fit_transform(X_train.reshape(1, -1), unseen.reshape(1, -1)).astype(int)
    return unseen_scaled
    
def svm_train(X, y, gamma=0.001, C=100):
    # instantiating an SVM classifier
    md_clf = svm.SVC(gamma=0.001, C=100.)

    # apply SVM to training data and draw boundaries.
    md_clf.fit(X, y)
    # a prediction for the test data point.
    return md_clf

def pca_svm_pred(imfile, md_pca, md_clf, dim1=45, dim2=60):
    im = mpimg.imread(imfile)
    im_flat = interpol_im(im, dim1=dim1, dim2=dim2, plot_new_im=True)
    im_flat_proj = md_pca.transform(im_flat.reshape(1, -1))
    pre = md_clf.predict(im_flat_proj.reshape(1, -1))
    return pre