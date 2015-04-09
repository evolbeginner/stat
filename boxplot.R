args <- commandArgs(trailingOnly = TRUE)
infile1 = args[1]
infile2 = args[2]

a <- scan(infile1,what='character')
b <- scan(infile2,what='character')

a=as.numeric(a)
b=as.numeric(b)

t.test(na.omit(a),na.omit(b))
boxplot(a,b, col=c('white','lightgrey'), outline=FALSE)

