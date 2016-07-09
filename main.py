import KeepBeingYou as isyana
import LDR
import TetapDalamJiwa as tdj
import KaliKedua as raisa
import TotalEclipse as bonnie
import CarelessWhisper as george
import wavelet as wv
import plotSignal as plt
from operator import itemgetter

def metodeWavelet(fullSong, potongan, namaLaguAsli, namaCutSong):
	signalCorrelate = wv.signalCorrelate(fullSong, potongan)
	crossCorrelation = wv.crossCorrelation(fullSong, potongan)
	maximumPeak = max(crossCorrelation)
	magnitude = wv.magnitude(crossCorrelation)

	#print "Magnitude: ", magnitude

	#plt.plotSignal(fullSong, potongan, signalCorrelate, namaLaguAsli, namaCutSong)

	return maximumPeak

	

#namaCutSong = "Isyana Sarasvati - Keep Being You"
#potongan = wv.waveletTransform(isyana.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(isyana.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(isyana.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(isyana.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(isyana.cutSong5) #potongan 50%

namaCutSong = "Isyana Sarasvati - Tetap Dalam Jiwa"
potongan = wv.waveletTransform(tdj.cutSongCoverKesamus) #cover song  Kesamus KENA!!!
#potongan = wv.waveletTransform(tdj.cutSongCoverSatria) #cover song  Satria gk kena
potongan = wv.waveletTransform(tdj.cutSongCoverAllfy) #cover song  ALLFy KENA!!!
#potongan = wv.waveletTransform(tdj.cutSongCoverAndri) #cover song  andri gk kena
#potongan = wv.waveletTransform(tdj.cutSongGitar) #accoustic gak kena
#potongan = wv.waveletTransform(tdj.cutSongHarry) #cover song jandre
#potongan = wv.waveletTransform(tdj.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(tdj.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(tdj.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(tdj.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(tdj.cutSong5) #potongan 50%

#namaCutSong = "Raisa - Kali Kedua"
#potongan = wv.waveletTransform(raisa.recordSong) #potongan record song
#potongan = wv.waveletTransform(raisa.cutSong6) #potongan 1%
#potongan = wv.waveletTransform(raisa.cutSong7) #potongan 2%
#potongan = wv.waveletTransform(raisa.cutSong8) #potongan 3%
#potongan = wv.waveletTransform(raisa.cutSong9) #potongan 4%
#potongan = wv.waveletTransform(raisa.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(raisa.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(raisa.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(raisa.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(raisa.cutSong5) #potongan 50%


#namaCutSong = "Raisa - LDR"
#potongan = wv.waveletTransform(LDR.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(LDR.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(LDR.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(LDR.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(LDR.cutSong5) #potongan 50%

#namaCutSong = "Bonnie - Total Eclipse of The Heart"
#potongan = wv.waveletTransform(bonnie.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(bonnie.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(bonnie.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(bonnie.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(bonnie.cutSong5) #potongan 50%

#namaCutSong = "George - Careless Whisper"
#potongan = wv.waveletTransform(george.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(george.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(george.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(george.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(george.cutSong5) #potongan 50%

"""Buat cari satu-satu"""
#fullSong = wv.waveletTransform(isyana.fullSong)
#fullSong = wv.waveletTransform(bonnie.fullSong)
#fullSong = wv.waveletTransform(raisa.fullSong)
#fullSong = wv.waveletTransform(george.fullSong)

"""Buat bandingin semua lagu"""
namaFullSong1 = "Isyana Sarasvati- Keep Being You"
namaFullSong2 = "Raisa - Kali Kedua"
namaFullSong3 = "Bonnie - Total Eclipse of The Heart"
namaFullSong4 = "George - Careless Whisper"
namaFullSong5 = "Raisa - LDR"
namaFullSong6 = "Isyana Sarasvati - Tetap Dalam Jiwa"
fullSong1 = wv.waveletTransform(isyana.fullSong)
fullSong2 = wv.waveletTransform(bonnie.fullSong)
fullSong3 = wv.waveletTransform(raisa.fullSong)
fullSong4 = wv.waveletTransform(george.fullSong)
fullSong6 = wv.waveletTransform(tdj.fullSong)

print "Input  : ", namaCutSong

hasilRaisa = (namaFullSong2, metodeWavelet(fullSong3, potongan, namaFullSong2, namaCutSong))
hasilBonnie = (namaFullSong3, metodeWavelet(fullSong2, potongan, namaFullSong3, namaCutSong))
hasilIsyana = (namaFullSong1, metodeWavelet(fullSong1, potongan, namaFullSong1, namaCutSong))
hasilGeorge= (namaFullSong4, metodeWavelet(fullSong4, potongan, namaFullSong4, namaCutSong))
hasilTDJ = (namaFullSong6, metodeWavelet(fullSong6, potongan, namaFullSong6, namaCutSong))

#print hasilRaisa

hasil = [hasilRaisa, hasilBonnie, hasilIsyana, hasilGeorge, hasilTDJ]

classifier = sorted(hasil, key=lambda x: x[1], reverse = True)

#print classifier

print "Output : ", classifier[0][0]


