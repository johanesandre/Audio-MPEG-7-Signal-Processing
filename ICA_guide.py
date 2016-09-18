from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
import fullSongPop as lagupop
import numpy
numpy.set_printoptions(threshold=numpy.nan)
numpy.seterr(divide='ignore', invalid='ignore')

time = np.linspace(0, 10, 2000)
s1 = np.sin(2 * time) # Signal 1 : sinusoidal signal
s2 = np.sign(np.sin(3 * time)) # Signal 2 : square signal
S = np.c_[s1, s2]
S += 0.2 * np.random.normal(size=S.shape) # Add noise
S /= S.std(axis=0) # Standardize data
 # Mix data
A = np.array([[1, 1], [0.5, 2]]) # Mixing matrix
 X = np.dot(S, A.T) # Generate observations

>>> # Compute ICA
>>> ica = decomposition.FastICA()
>>> S_ = ica.fit(X).transform(X) # Get the estimated sources
>>> A_ = ica.get_mixing_matrix() # Get estimated mixing matrix
>>> np.allclose(X, np.dot(S_, A_.T))
