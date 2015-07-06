#! /bin/env python

import scipy.stats
import sys
import getopt
import re


#############################################################################
inputs = []
selected_test = "shapiro"
sep = "\t"

values = {}
legal_tests = ["shapiro", "ks"]
# ["ad", "cvm", "sf", "dago"]


#############################################################################
def read_input(input, sep="\t", values={}):
    num_of_values_already = len(values)
    with open(input) as fh:
        for line in fh:
            line = line.rstrip('\n\r')
            for index,ele in enumerate(re.split(sep,line)):
                order = index + num_of_values_already
                if order not in values:
                    values[order]=[]
                if ele == '':
                    continue
                values[order].append(float(ele))
    return(values)


#############################################################################
"""
    shapiro Shapiro-Wilk test
    ks      Kolmogorov-Smirnov test
    ad      Anderson-Darling
    cvm     Cramer-von Mises test
    sf      Shapiro-Francia test
    dago    D'Agostino test
"""


opts, args = getopt.getopt(
    sys.argv[1:],
    '-i:',
    ["in=", 'type=', 'test=', "sep="],
)

for opt, value in opts:
    if opt == "--type" or opt == "--test":
        if not value in legal_tests:
            print "Legal tests are" + " ".join(legal_tests)
            sys.exit()
        else:
            selected_test = value
    elif opt == "-i" or opt == "--in":
        inputs.append(value)
    elif opt == "--sep":
        sep = value
    else:
        raise "illegal params!"


#############################################################################
for input in inputs:
    values = dict(values, **read_input(input, sep, values))

print selected_test

for index, value in values.iteritems():
    if selected_test == "shapiro":
        print scipy.stats.shapiro(value)
    elif selected_test == "ks":
        print scipy.stats.kstest(value, 'norm')
        

