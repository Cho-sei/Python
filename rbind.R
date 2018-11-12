sub3=0
for (i in dir("sub3"))
{
	filename = paste("sub3/",i,sep="")
	data = read.csv(filename,header=F)
	sub3 = rbind(sub3,data)
}
sub3[-1,]