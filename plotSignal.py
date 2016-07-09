import matplotlib.pyplot as plt

def plotSignal(cDFull, cDPotongan, crossCorrelate, namaLagu, namaPotongan):
	fig, (ax_orig, ax_noise, ax_corr1) = plt.subplots(3, 1, sharex=True)
	ax_noise.plot(cDFull)
	ax_noise.set_title('FULL SONG '+ namaLagu)

	ax_orig.plot(cDPotongan)
	ax_orig.set_title('CUT SONG ' + namaPotongan)

	#pakaiFFT = signal.fftconvolve(fullSong, cutSong1[::-1], mode='full')
	ax_corr1.plot(crossCorrelate)
	ax_corr1.axhline(0.5, ls=':')
	ax_corr1.set_title("CROSS-CORRELATION")

	ax_orig.margins(0,0.1)
	fig.tight_layout()
	fig.show()
