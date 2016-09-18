import nimfa
import fullSongPop as lagupop

matrix = lagupop.apalah
nmf= nimfa.nmf(matrix,seed="random_vcol",rank=2,max_iter=2000)
fit= nmf()
w=fit.basis()
H=fit.coef()

#print nmf
