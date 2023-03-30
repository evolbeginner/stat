#! /bin/env Rscript


############################################
library(getopt)


############################################
infile <- NA
is_header <- F
field <- c(1,2)
sep <- '\t'

test <- 'ttest'
paired <- F


############################################
spec = matrix(c(
	'infile', 'i', '2', 'character',
	'header', 'h', '0', 'logical',
	'field', 'f', '2', 'character',
	'sep', 's', '2', 'character',
	'test', 't', '2', 'character',
	'paired', 'p', '0', 'logical'),
	ncol=4, byrow=T
)

opt <- getopt(spec)

#if(!is.null(opt$header)){
if(!is.null(opt$infile)){
	infile <- opt$infile
}
if(!is.null(opt$header)){
	is_header <- T
}
if(!is.null(opt$field)){
	field <- as.numeric(unlist(strsplit(opt$field, ',')))
}
if(!is.null(opt$sep)){
	sep <- opt$sep
}
if(!is.null(opt$test)){
	test <- opt$test
}
if(!is.null(opt$paired)){
	paired <- T
}


############################################
df <- read.table(infile, sep=sep, header=is_header, stringsAsFactors=F)

all_pairs <- combn(field,2)


############################################
if(grepl('ttest', test)){
	test_func <- t.test
} else if(grepl('wilcox', test)){
	test_func <- wilcox.test
} else{
	print(paste("Unknown test", test))
	q(status=1)
}

f <- function(col_nums, test_func){
	res <- test_func(df[,col_nums[1]], df[,col_nums[2]], paired=paired)
	return(paste(paste(col_nums, collapse='-'), round(res$p.value,4), sep=":"))
}

cat(apply(all_pairs, 2, f, test_func), sep='\t')
cat("\n")
#func(df$V1, df, paired)


