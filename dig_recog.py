from scipy.interpolate import interp2d
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import transform, data, io


dig_data = load_digits()
X = dig_data.data
y = dig_data.target

md_clf = svm_train(X[0:60], y[0:60])
perc = 0
mis = 0
tot_start = 60
tot_end = 80
for i in range(tot_start, tot_end):
    ans = y[i]
    pre = md_clf.predict(X[i].reshape(1, -1))[0]
    if ans != pre:
        plt.imshow(X[i].reshape((8, 8)), cmap='binary')
        plt.show()
        print("--------> index, actual digit, svm_prediction: {:d}, {:d}, {:d}".format(i, ans, pre))
    if ans == pre:
        perc += 1.
        
percentage = (perc/(tot_end-tot_start))*100.
print("Total number of mis-identifications: {:d}".format(mis))
print("Success rate: {:f}".format(percentage))

############################################################################
############################## unseen_dig.png ##############################
############################################################################

unseen = mpimg.imread('unseen_dig.png')
unseen_flat = interpol_im(unseen, plot_new_im=True)

plt.imshow(X[15].reshape((8, 8)), cmap='binary')
plt.show()

unseen_scaled = rescale_pixel(X, unseen_flat, ind=15)

unseen_pre = md_clf.predict(unseen_flat.reshape(1, -1))
unseen_scaled_pre = md_clf.predict(unseen_scaled.reshape(1, -1))
print("Predictions for unscaled and scaled unseen image: {:d}, {:d}".format(unseen_pre[0], unseen_scaled_pre[0]))