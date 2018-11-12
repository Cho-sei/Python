C.candidate = exp(seq(log(100),log(0.1),length.out=20))
sigma.candidate = exp(seq(log(10),log(0.01),length.out=20))
N.C = length(C.candidate)
N.sigma = length(sigma.candidate)

CROSS = matrix(0,N.C,N.sigma)
for(i in 1:N.C){
	for(j in 1:N.sigma){
		C = C.candidate[i]
		sigma = sigma.candidate[j]
		fit = ksvm(y~.,data=train.data,kernel="polydot",sigma=sigma,C=C,cross=N)
		CROSS[i,j] = fit@cross
	}
}

index = which.min(CROSS)
index = arrayInd(index,.dim=c(20,20))
index_C = index[1]
index_sigma = index[2]
fit = ksvm(y~.,data=train.data, kernel="rbfdot",sigma=sigma.candidate[index_sigma],C=C.candidate[index_C],cross=N)

result = predict(fit,test.data)
table(Correct.label,result)