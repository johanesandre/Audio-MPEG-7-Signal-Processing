from sklearn.decomposition import PCA
import numpy
import fullSongPop as lagupop
nf = 100
pca = PCA(n_components=nf)
X = numpy.array(lagupop.apalah)
X= numpy.reshape(1,-1)
pca.fit(X)

X_new = pca.transform(X)
print X_new