#! /bin/env Rscript


###########################################################
is_paired = FALSE


###########################################################
args=commandArgs(T)

a = read.csv(args[1], sep="\t", colClasses=c('numeric'))

b = read.csv(args[2], sep="\t", colClasses=c('numeric'))

if(args[4]>0){
	is_paired = TRUE
}


###########################################################
if (args[3] == 'w'){
	wilcox.test(a[,1], b[,1], paired=is_paired, alternative="two.sided")
}

if (args[3] == 't'){
	t.test(a[,1], b[,1], paired=is_paired, alternative="two.sided")
}


