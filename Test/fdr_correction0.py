#! /bin/env python

import getopt
import sys

import statsmodels.sandbox.stats.multicomp


###############################################################
infile = None
num_str = None
#method = 'i'
method = 'fdr_bh'

# i or p for fdr_bh, n for fdr_by
'''
    bonferroni : one-step correction
    sidak : one-step correction
    holm-sidak : step down method using Sidak adjustments
    holm : step-down method using Bonferroni adjustments
    simes-hochberg : step-up method (independent)
    hommel : closed method based on Simes tests (non-negative)
    fdr_bh : Benjamini/Hochberg (non-negative)
    fdr_by : Benjamini/Yekutieli (negative)
    fdr_tsbh : two stage fdr correction (non-negative)
    fdr_tsbky : two stage fdr correction (non-negative)
'''


nums = []


###############################################################
try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        "i:",
        ["num=", "method="],
    )
except getopt.GetoptError as err:
    print str(err)
    sys.exit(2)
for opt, value in opts:
    if opt == '-i':
        infile = value
    elif opt in ('--num'):
        num_str = value
    elif opt in ('--method'):
        method = value
    else:
        assert False, "unhandled option"
    # ...


###############################################################
if infile:
    in_fh = open(infile, 'r')
    for line in in_fh:
        line = line.rstrip('\n\r')
        line_arr = line.split(',')
        line_arr = map(lambda x: float(x), line_arr)
        nums.extend(line_arr)
    in_fh.close()
elif num_str:
    for i in num_str.split(','):
        nums.append(float(i))
else:
    print "Wrong! Exiting ......"
    sys.exit(1)

#res = statsmodels.sandbox.stats.multicomp.fdrcorrection0(nums, method=method)
res = statsmodels.stats.multitest.multipletests(nums, method=method)

fdrs = res[1]
print ",".join(map(lambda x: str(x), fdrs))


