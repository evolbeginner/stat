args <- commandArgs(trailingOnly = TRUE)

error.bar <- function(x, y, upper, lower=upper, length=0.1,...){
if(length(x) != length(y) | length(y) !=length(lower) | length(lower) != length(upper))
stop("vectors must be same length")
arrows(x,y+upper, x, y-lower, angle=90, code=3, length=length, ...)
}

#######################################################################################
infile1 = args[1]
infile2 = args[2]
#x.label = args[3]
y.label = args[3]

a <- scan(infile1,what='character')
b <- scan(infile2,what='character')
a=as.numeric(a)
b=as.numeric(b)
a=na.omit(a)
b=na.omit(b)
c<-c(0)

x=matrix(a)
y=matrix(b)
c=matrix(c)

x.means <- apply(x,2,mean)
x.sd <- apply(x,2,sd)
y.means <- apply(y,2,mean)
y.sd <- apply(y,2,sd)

yy <- matrix(c(c,x.means,c,y.means,c),5,byrow=TRUE)
ee <- matrix(c(c,x.sd,c,y.sd,c),5,byrow=TRUE)*1.96/10

upper_limit=max(x.means+1.1*x.sd, y.means+1.1*y.sd)

barx <- barplot(yy, beside=TRUE,col=c('white','white','white',"lightgrey"), ylim=c(0,upper_limit), axis.lty=1, ylab=y.label)
error.bar(barx,yy,ee)

