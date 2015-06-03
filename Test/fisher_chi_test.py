#! /bin/env python

import scipy as sp
import scipy.stats
import sys
import re
import getopt
import itertools


#########################################################################
numbers = []
class_numbers = []
list = []
type = None
results = None


opts, args = getopt.getopt(
    sys.argv[1:],
    "",
    ["num=","number=","numbers=","class_num=","type="],
)

for opt, value in opts:
    if opt == "--num" or opt == "--number" or opt == "--numbers":
        for i in value.split(','):
            numbers.append(int(i))
    elif opt == "--class_num":
        for index, i in enumerate(value.split(' ')):
            class_numbers.append([])
            for j in i.split(','):
                class_numbers[index].append(int(j))
    elif opt == "--type":
        type = value


#########################################################################
if numbers:
    list = [numbers[0], numbers[2]-numbers[0], numbers[1], numbers[3]-numbers[1]]
    x = [list[0:2],list[2:4]]
    if type == "fisher":
        results = sp.stats.fisher_exact(x)
    elif type == "chi":
        results = sp.stats.chi2_contingency(x)
elif class_numbers:
    x=class_numbers
    if type == "fisher":
        print "Error! class_num cannot be applied to Fisher exact test! Exiting ......"
        sys.exit()
    elif type == "chi":
        results = sp.stats.chi2_contingency(x)

print results[1]


