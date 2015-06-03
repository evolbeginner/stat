#! /bin/env python

from scipy import stats
import sys

####################################
input = sys.argv[1]
if len(sys.argv) > 2:
    p = float(sys.argv[2])
else:
    p = 0.5

in_fh = open(input, 'r')
for line in in_fh.readlines():
    line = line.rstrip('\n\r')
    num1, num2 = map(lambda x: float(x), line.split('\t'))
    print stats.binom_test(num1, num1+num2, p)
    #print stats.binom.sf(num1, num1+num2, p)
in_fh.close()

