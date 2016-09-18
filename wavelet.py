from scipy import signal
import numpy as np
import pywt

def waveletTransform(lagu):
	cA, cD = pywt.dwt(lagu, 'db1')

	return cD

def signalCorrelate(fullLagu, potonganLagu):
	signalCorrelate = signal.correlate(fullLagu, potonganLagu, mode='full')

	return signalCorrelate

def crossCorrelation(fullLagu, potonganLagu):
	hasilCross = np.correlate(fullLagu, potonganLagu)

	return hasilCross

def magnitude(crossCorrelation):
	magnitude = np.sqrt(crossCorrelation.dot(crossCorrelation))

	return magnitude
