import KeepBeingYou as isyana
import LDR
import TetapDalamJiwa as tdj
import KaliKedua as raisa
import TotalEclipse as bonnie
import CarelessWhisper as george
import fullSongJazz as lagujazz
import fullSongPop as lagupop
import fullSongRap as lagurap
import fullSongRock as lagurock
import fullSongDugem as lagudugem
import fullSongClassic as laguclassic
import wavelet as wv
import plotSignal as plt
#import envelopePop as eps
from operator import itemgetter
import fullSongPop as PopSongs
import numpy as np
import PCA_LAGI_TES as pca
import matplotlib.pyplot as plt

np.set_printoptions(threshold=np.nan)


potongan = 	wv.waveletTransform(isyana.cutSong4)
#print potongan
hasil = np.fft.fft(potongan)
#print np.fft.fft
print hasil
print "---------------"
print potongan

'''
t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)
plt.show()
'''