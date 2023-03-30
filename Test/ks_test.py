#! /bin/env python

# script to do Kormogorov-Simirnov test

#####################################################
from scipy.stats import ks_2samp
import sys

#####################################################
def read_list(list_file):
    list = []
    for line in open(list_file, 'r').readlines():
        line = line.rstrip('\n\r')
        list.append(float(line.split("\t")[0]))
    return(list)


#####################################################
list1 = read_list(sys.argv[1])
list2 = read_list(sys.argv[2])

print ks_2samp(list1, list2)[1]

