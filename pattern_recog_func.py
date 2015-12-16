from scipy.interpolate import interp2d
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits

def interpol_im(im, dim1=8, dim2=8, plot_new_im=False, cmap='binary', axis_off=False):
    f2d = interp2d(dim1, dim2, im)
    
    if plt_new_im:
        plt.imshow(f2d, cmap=cmap, interpolation='nearest')
        plt.grid('off')
        plt.show()
        
    f2d_flat = f2d.flatten()
    return f2d_flat

def pca_X(X, n_comp=10):
    md_pca = PCA(n_comp)
    X_proj = pca.fit_transform(X)
    return md_pca, X_proj

def rescale_pixel(X, unseen, ind=0):
    dig_data = load_digits()
    X[ind] = dig_data.data

# def pca_svm_pred(imfile, md_pca, md_clf, dim1=45, dim2=60):
#     im = mpimg.imread(imfile)
#     f2d_flat = interpol_im(im, dim1=dim1, dim2=dim2)
    
#     clf = svm.SVC(kernel='linear')