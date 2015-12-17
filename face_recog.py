"""
The following program performs the simplest possible facial recognition.  The program perpares 21 given images of two different physicists, interpolates them onto a 45/60 grid, then creates a data array that contains all the flattened images, our dataset, X, throughout the entire program.  It first performs principle component analysis (PCA) on the 21 images, trains them, creating a classifier.  Validation is done through the leave-one-out (LOO) method.  Finally, it prints the success rate.  Ultimately, the program tests by using two unseen images of the two different physicists, performs interpolation, PCA projection, classification, and then prediction, printing out its prediction for both the images and displaying them for human inspection.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pattern_recog_func import interpol_im
from pattern_recog_func import pca_X
from pattern_recog_func import rescale_pixel
from pattern_recog_func import svm_train
from pattern_recog_func import pca_svm_pred
from pdb import set_trace
from scipy.interpolate import interp2d
from skimage import transform, data, io
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn import preprocessing
from sklearn import svm


bohr = 10
ein = 11
flat_bohr = []
flat_ein = []
y = []
phys_dict = {0: 'Bohr', 1: 'Einstein'}

for i in range(bohr):
    im = mpimg.imread('bohr'+str(i)+'.jpeg')
    flat_bohr.append(interpol_im(im, dim1=45, dim2=60, plot_new_im=False, cmap='binary', axis_off=True))
    y.append(0)
for i in range(ein):
    im = mpimg.imread('ein'+str(i)+'.jpeg')
    flat_ein.append(interpol_im(im, dim1=45, dim2=60, plot_new_im=False, cmap='binary', axis_off=True))
    y.append(1)
    
X = np.vstack((np.array(flat_bohr), np.array(flat_ein)))

md_pca, X_proj = pca_X(X)

perc = 0
tot = 21

for select_idx in range(tot):
#     set_trace()
    Xtrain = np.delete(X, select_idx, axis = 0)
    ytrain = np.delete(y, select_idx)
    
    md_pca.fit(Xtrain)
    Xtrain_proj = md_pca.transform(Xtrain)

    Xtest = X[select_idx].reshape(1, -1)
    ytest = y[select_idx]
    Xtest_proj = md_pca.transform(Xtest)

    md_clf = svm_train(Xtrain_proj, ytrain)
    pre = md_clf.predict(Xtest_proj)
    if pre == ytest:
        perc += 1.
        
perc /= (tot/100.)
print('Success rate: {:f}'.format(perc))

unseen_phys1 = 'unseen_phys1.jpg'
unseen_phys2 = 'unseen_phys2.jpg'

pre1 = pca_svm_pred(unseen_phys1, md_pca, md_clf)
pre2 = pca_svm_pred(unseen_phys2, md_pca, md_clf)

pre_ein_statement = 'PCA+SVM prediction for physicist 1: {:s}'.format(phys_dict[pre1[0]])
pre_bohr_statement = 'PCA+SVM prediction for physicist 2: {:s}'.format(phys_dict[pre2[0]])

print(pre_ein_statement)
print(pre_bohr_statement)