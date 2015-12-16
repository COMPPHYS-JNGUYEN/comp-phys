from scipy.interpolate import interp2d
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import transform, data, io
from pattern_recog_func import interpol_im
from pattern_recog_func import pca_X
from pattern_recog_func import rescale_pixel
from pattern_recog_func import svm_train
from pattern_recog_func import pca_svm_pred

dig_data = load_digits()
X = dig_data.data
y = dig_data.target

print(X[15].shape)
print(y)

unseen = mpimg.imread('unseen_dig.png')
flat = interpol_im(unseen, plot_new_im=True)
dig_data = load_digits()
X = dig_data.data
X_flat = interpol_im(X[15], plot_new_im=True)