from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
#from sklearn import PCA
import numpy as np

x1 = np.random.normal(size=100)
x2 = np.random.normal(size=100)
x3 = x1 + x2

X = np.c_[x1, x2, x3]
print x3
print X

pca = decomposition.PCA()
pca.fit(X)
#PCA(copy=True, n_components=None, whiten=False)
print pca.explained_variance_