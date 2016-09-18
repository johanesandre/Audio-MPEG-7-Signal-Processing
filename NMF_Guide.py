from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import ProjectedGradientNMF
from sklearn import decomposition
import fullSongPop as lagupop
import fullSongJazz as lagujazz
import numpy
numpy.set_printoptions(threshold=numpy.nan)
numpy.seterr(divide='ignore', invalid='ignore')

x1= lagupop.apalah
X=numpy.array(x1)
model = ProjectedGradientNMF(n_components=1,init = 0)
model.fit(X)

print model.components_