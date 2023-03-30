#! /bin/env Rscript


library('lmtest')


##################################################################################
args <- commandArgs(trailingOnly = TRUE)

if (length(args) < 4){
	print ("At least four arguments should be given! Exiting ......")
	q()
}

half_length = length(args)/2

if (length(args) %% 2 != 0){
	print ("The number of arguments has to be an even. Exiting ......")
	q()
}


##################################################################################
a1 = args[1:half_length]
a2 = args[(half_length+1):length(args)]

mat = c(a1,a2)

w = rep(0, length(args))

z = rep(1:0, each=half_length)

m1<-lm(mat~w)

m2<-lm(mat~z)

lrtest(m1,m2)
