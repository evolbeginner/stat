#! /bin/env python

from scipy import stats
import sys


####################################
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
if len(sys.argv) > 3:
    p = float(sys.argv[3])
else:
    p = 0.5

print stats.binom_test(num1, num1+num2, p)
print 1-stats.binom.sf(num1, num1+num2, p)

