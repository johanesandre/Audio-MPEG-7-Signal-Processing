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
import numpy
import PCA_LAGI_TES as pca
numpy.set_printoptions(threshold=numpy.nan)

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

#namaCutSong = "Isyana Sarasvati - Tetap Dalam Jiwa"
#potongan = wv.waveletTransform(tdj.cutSongCoverKesamus) #cover song  Kesamus Gk KENA!!!
#potongan = wv.waveletTransform(tdj.cutSongCoverSatria) #cover song  Satria gk kena --> KENA DENGAN INSTRUMEN
#potongan = wv.waveletTransform(tdj.cutSongCoverAllfy) #cover song  ALLFy KENA!!! -->Dengan Instrumen gak kena
#potongan = wv.waveletTransform(tdj.cutSongCoverAndri) #cover song  andri gk kena
#potongan = wv.waveletTransform(tdj.cutSongGitar) #accoustic gak kena
#potongan = wv.waveletTransform(tdj.cutSongHarry) #cover song jandre gak kena
#potongan = wv.waveletTransform(tdj.cutSong1) #potongan 5%
#potongan = wv.waveletTransform(tdj.cutSong2) #potongan 10%
#potongan = wv.waveletTransform(tdj.cutSong3) #potongan 20%
#potongan = wv.waveletTransform(tdj.cutSong4) #potongan 30%
#potongan = wv.waveletTransform(tdj.cutSong5) #potongan 50%

#namaCutSong = "Raisa - Kali Kedua"
#potongan = wv.waveletTransform(raisa.cutSongCoverRamDhan) #potongan cover song kena dengan instrumen
#potongan = wv.waveletTransform(raisa.cutSongCoverBintang) #potongan cover song kena dengan instrumen
#potongan = wv.waveletTransform(raisa.recordSong) #potongan record song
#potongan = wv.waveletTransform(raisa.cutSongLiveVI) #potongan instrumen live Kena
#potongan = wv.waveletTransform(raisa.cutSong6) #potongan 1% gak kena
#potongan = wv.waveletTransform(raisa.cutSong7) #potongan 2% gak kena
#potongan = wv.waveletTransform(raisa.cutSong8) #potongan 3% kena
#potongan = wv.waveletTransform(raisa.cutSong9) #potongan 4% kena
#potongan = wv.waveletTransform(raisa.cutSong1) #potongan 5% kena
#potongan = wv.waveletTransform(raisa.cutSong2) #potongan 10% kena 
#potongan = wv.waveletTransform(raisa.cutSong3) #potongan 20% kena 
#potongan = wv.waveletTransform(raisa.cutSong4) #potongan 30% kena 
#potongan = wv.waveletTransform(raisa.cutSong5) #potongan 50% kena


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

#envelope1 = pca.pca2(lagupop.envelope)
#envelope1= numpy.array(lagupop.apalah)
#print envelope1,len(envelope1)
#envelope1=envelope1
#cobaPCA= pca.pca2(envelope1)
#print cobaPCA,len(cobaPCA)
#cobaEnvelope = wv.waveletTransform(envelope1)
#print cobaEnvelope,len(cobaEnvelope)
		
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
namaFullSong7 = "Everybody Knew"
namaFullSong8 = "Pergi untuk kembali"
namaFullSong9 = "Kolam susu"
namaFullSong10 = "Menghujam Jantungku"
namaFullSong11 = "Sedari Dulu"
namaFullSong12 = "Thing will get better"
namaFullSong13 = "Firasat"
namaFullSong14 = "Terjebak Nostalgia"
namaFullSong15 = "Apalah"
namaFullSong16 = "Move on"
namaFullSong17 = "Jomblo"
namaFullSong18 = "Narsis"
namaFullSong19 = "F3"
namaFullSong20 = "Seaside"
namaFullSong21 = "Online"
namaFullSong22 = "I Know You Want Me"
namaFullSong23 = "On The Floor"
namaFullSong24 = "DJ Snake"
namaFullSong25 = "Mr Saxobeat"
namaFullSong26 = "Faded"
namaFullSong27 = "Its My Life"
namaFullSong28 = "Livin on a Prayer"
namaFullSong29 = "Somewhere I Belong"
namaFullSong30 = "From Whom The Bell"
namaFullSong31 = "Whiskey in The Jar"
namaFullSong32 = "Bach Air On"
namaFullSong33 = "Beethoven"
namaFullSong34 = "Jean Joset Mouret"
namaFullSong35 = "Mozzart Alegro"
namaFullSong36 = "Mozzart Andate"


'''
fullSong1 = wv.waveletTransform(isyana.fullSong)
fullSong2 = wv.waveletTransform(bonnie.fullSong)
fullSong3 = wv.waveletTransform(raisa.fullSong)
fullSong4 = wv.waveletTransform(george.fullSong)
fullSong6 = wv.waveletTransform(tdj.fullSong)

fullsong7 = wv.waveletTransform(lagujazz.everybody_knew)
fullsong8 = wv.waveletTransform(lagujazz.pergi_untuk_kembali)
fullsong9 = wv.waveletTransform(lagujazz.kolam_susu)
fullsong10 = wv.waveletTransform(lagujazz.menghujam_jantungku)
fullsong11 = wv.waveletTransform(lagujazz.sedari_dulu)

fullsong12 = wv.waveletTransform(lagupop.things_will_get_better)
fullsong13 = wv.waveletTransform(lagupop.firasat)
fullsong14 = wv.waveletTransform(lagupop.terjebak_nostalgia)
fullsong15 = wv.waveletTransform(lagupop.apalah)
fullsong16 = wv.waveletTransform(lagupop.move_on)

fullsong17 = wv.waveletTransform(lagurap.jomblo)
fullsong18 = wv.waveletTransform(lagurap.narsis)
fullsong19 = wv.waveletTransform(lagurap.f3)
fullsong20 = wv.waveletTransform(lagurap.seaside)
fullsong21 = wv.waveletTransform(lagurap.online)

fullsong22 = wv.waveletTransform(lagudugem.i_know_you_want_me)
fullsong23 = wv.waveletTransform(lagudugem.on_the_floor)
fullsong24 = wv.waveletTransform(lagudugem.djsnake)
fullsong25 = wv.waveletTransform(lagudugem.mrsaxobeat)
fullsong26 = wv.waveletTransform(lagudugem.faded)

fullsong27 = wv.waveletTransform(lagurock.its_my_life)
fullsong28 = wv.waveletTransform(lagurock.livin_on_a_prayer)
fullsong29 = wv.waveletTransform(lagurock.somewhere_i_belong)
fullsong30 = wv.waveletTransform(lagurock.for_whom_the_bell)
fullsong31 = wv.waveletTransform(lagurock.whiskey_in_the_jar)

fullsong32 = wv.waveletTransform(laguclassic.bach_air_on)
fullsong33 = wv.waveletTransform(laguclassic.beethoven)
fullsong34 = wv.waveletTransform(laguclassic.jean_joset_mouret)
fullsong35 = wv.waveletTransform(laguclassic.mozart_allegro)
fullsong36 = wv.waveletTransform(laguclassic.mozart_andate)







print "Input  : ", namaCutSong

hasilRaisa = (namaFullSong2, metodeWavelet(fullSong3, potongan, namaFullSong2, namaCutSong))
hasilBonnie = (namaFullSong3, metodeWavelet(fullSong2, potongan, namaFullSong3, namaCutSong))
hasilIsyana = (namaFullSong1, metodeWavelet(fullSong1, potongan, namaFullSong1, namaCutSong))
hasilGeorge= (namaFullSong4, metodeWavelet(fullSong4, potongan, namaFullSong4, namaCutSong))
hasilTDJ = (namaFullSong6, metodeWavelet(fullSong6, potongan, namaFullSong6, namaCutSong))
hasilEveryBodyKnow = (namaFullSong7, metodeWavelet(fullsong7, potongan, namaFullSong7, namaCutSong))
hasilPergiUntukKembali = (namaFullSong8, metodeWavelet(fullsong8, potongan, namaFullSong8, namaCutSong))
hasilKolamSusu = (namaFullSong9, metodeWavelet(fullsong9, potongan, namaFullSong9, namaCutSong))
hasilMenghujamJantungku = (namaFullSong10, metodeWavelet(fullsong10, potongan, namaFullSong10, namaCutSong))
hasilSedariDulu = (namaFullSong11, metodeWavelet(fullsong11, potongan, namaFullSong11, namaCutSong))
hasilThingsWillGetBetter = (namaFullSong12, metodeWavelet(fullsong12, potongan, namaFullSong12, namaCutSong))
hasilFirasat = (namaFullSong13, metodeWavelet(fullsong13, potongan, namaFullSong13, namaCutSong))
hasilTerjebakNostalgia = (namaFullSong14, metodeWavelet(fullsong14, potongan, namaFullSong14, namaCutSong))
hasilApalah = (namaFullSong14, metodeWavelet(fullsong14, potongan, namaFullSong14, namaCutSong))
hasilMoveOn = (namaFullSong15, metodeWavelet(fullsong15, potongan, namaFullSong15, namaCutSong))
hasilJomblo = (namaFullSong16, metodeWavelet(fullsong16, potongan, namaFullSong16, namaCutSong))
hasilNarsis = (namaFullSong17, metodeWavelet(fullsong17, potongan, namaFullSong17, namaCutSong))
hasilF3 = (namaFullSong18, metodeWavelet(fullsong18, potongan, namaFullSong18, namaCutSong))
hasilFirasat = (namaFullSong19, metodeWavelet(fullsong19, potongan, namaFullSong19, namaCutSong))
hasilSeaside = (namaFullSong20, metodeWavelet(fullsong20, potongan, namaFullSong20, namaCutSong))
hasilOnline = (namaFullSong21, metodeWavelet(fullsong20, potongan, namaFullSong21, namaCutSong))
hasilIKnowYouWantMe = (namaFullSong22, metodeWavelet(fullsong22, potongan, namaFullSong22, namaCutSong))
hasilOntTheFloor = (namaFullSong23, metodeWavelet(fullsong23, potongan, namaFullSong23, namaCutSong))
hasilDJSnake = (namaFullSong24, metodeWavelet(fullsong24, potongan, namaFullSong24, namaCutSong))
hasilMrSaxobeat = (namaFullSong25, metodeWavelet(fullsong25, potongan, namaFullSong25, namaCutSong))
hasilFaded = (namaFullSong26, metodeWavelet(fullsong26, potongan, namaFullSong26, namaCutSong))
hasilItsMyLife = (namaFullSong27, metodeWavelet(fullsong27, potongan, namaFullSong27, namaCutSong))
hasilLivinOnAPrayer = (namaFullSong28, metodeWavelet(fullsong28, potongan, namaFullSong28, namaCutSong))
hasilSomewhereIBelong = (namaFullSong29, metodeWavelet(fullsong29, potongan, namaFullSong29, namaCutSong))
hasilFromWhomTheBell = (namaFullSong30, metodeWavelet(fullsong30, potongan, namaFullSong30, namaCutSong))
hasilWhiskeyInTheJar = (namaFullSong31, metodeWavelet(fullsong31, potongan, namaFullSong31, namaCutSong))
hasilBachAirOn = (namaFullSong32, metodeWavelet(fullsong32, potongan, namaFullSong32, namaCutSong))
hasilBeethoven = (namaFullSong33, metodeWavelet(fullsong33, potongan, namaFullSong33, namaCutSong))
hasilJeanJoset = (namaFullSong34, metodeWavelet(fullsong34, potongan, namaFullSong34, namaCutSong))
hasilMozzartAlegro = (namaFullSong35, metodeWavelet(fullsong35, potongan, namaFullSong35, namaCutSong))
hasilMozzartAndate = (namaFullSong36, metodeWavelet(fullsong36, potongan, namaFullSong36, namaCutSong))

hasil = [hasilRaisa, hasilBonnie, hasilIsyana, hasilGeorge, hasilTDJ, hasilEveryBodyKnow, hasilPergiUntukKembali, hasilKolamSusu, hasilMenghujamJantungku, hasilSedariDulu,hasilThingsWillGetBetter,hasilFirasat,hasilSeaside,hasilOnline,hasilIKnowYouWantMe,hasilOntTheFloor,hasilDJSnake,hasilMrSaxobeat,hasilFaded,hasilItsMyLife,hasilLivinOnAPrayer,hasilSomewhereIBelong,hasilFromWhomTheBell,hasilWhiskeyInTheJar,hasilBachAirOn,hasilBeethoven,hasilJeanJoset,hasilMozzartAndate,hasilMozzartAlegro]

classifier = sorted(hasil, key=lambda x: x[1], reverse = True)

#print classifier

print "Output : ", classifier[0][0]
'''

