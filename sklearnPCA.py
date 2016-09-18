from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
import fullSongPop as lagupop
import numpy
numpy.set_printoptions(threshold=numpy.nan)
numpy.seterr(divide='ignore', invalid='ignore')


#X= numpy.array(lagupop.apalah).reshape((len(lagupop.apalah)),-1)

X= numpy.array(lagupop.apalah).reshape(1,-1)
#print X
#print type(X)
#X= numpy.array(lagupop.envelope)
X_std = StandardScaler().fit_transform(X)
sklearn_pca = sklearnPCA(n_components=2)
Y_sklearn = sklearn_pca.fit_transform(X_std)


#print Y_sklearn
print X_std,len(Y_sklearn)