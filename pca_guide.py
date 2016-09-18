from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
#import fullSongPop as lagupop
#import fullSongJazz as lagujazz
import numpy
import ASP_Classic as laguclassic
import ASP_Dugem as lagudugem
import ASP_Jazz as lagujazz
import ASP_Rap as lagurap
#import ASP_Rock as lagurock
import ASP_EDM as laguedm
import ASP_Rock2 as lagurock
import ASP_Pop as lagupop
import wavelet as wv

numpy.set_printoptions(threshold=numpy.nan)
numpy.seterr(divide='ignore', invalid='ignore')
#PCA(copy=True, n_components=None, whiten=False)
#x1=lagupop.envelope
'''
x1 = numpy.random.normal(size=100)
x2 = numpy.random.normal(size=100)
x3 = x1 + x2
X = numpy.c_[x1, x2, x3]
print X
'''

#wavelet=wv.waveletTransform(lagurock.idisappear)
x1=numpy.array(lagurock.battery)
x1=numpy.array(x1)
#X=numpy.array(x1).reshape(1,-1)
X=numpy.c_[x1] #dipisah2
#print X
pca=decomposition.PCA()
pca.fit(X)
#print x1
print pca.explained_variance_
#print X

pca.n_components = 1
X_reduced = pca.fit_transform(X)
X_reduced.shape
#print X_reduced,len(X_reduced)
