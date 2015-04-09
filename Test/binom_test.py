#! /bin/env python


from scipy import stats
import sys

####################################
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print stats.binom_test(num1, num1+num2)

