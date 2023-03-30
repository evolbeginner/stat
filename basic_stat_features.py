#! /bin/env python

import numpy as np
import getopt
import sys
import re
from functools import partial


##################################################
def read_input(input, sep="\t", values={}, fields=[]):
    num_of_values_already = len(values)
    if input == '-':
        fh = sys.stdin
    else:
        fh = open(input, 'r')
    for line in fh:
        line = line.rstrip('\n\r')
        for index,ele in enumerate(re.split(sep,line)):
            if fields:
                if not index in fields:
                    continue
            order = index + num_of_values_already
            if order not in values:
                values[order]=[]
            if ele == '' or not re.search('[0-9]', ele):
                continue
            values[order].append(float(ele))
    return(values)


def output_values(value_array, value_array_name, is_with_title=False, is_title_diff_line=False):
    if is_with_title:
        print value_array_name,
    if is_title_diff_line:
        print
    else:
        if is_with_title:
            print "\t",
        else:
            pass
    print "\t".join(map(lambda x: str(x), value_array))


def get_median(a):
    if len(a) < 1:
        return None
    else:
        b = sorted(a)
        return b[len(b) // 2]


##################################################
is_all = False
is_mean = False
is_std = False
is_se = False
is_median = False
is_limits = False
is_max = False
is_min = False
is_count = False
sep = "\t"
inputs = []
fields = []
is_with_title = False
is_title_diff_line = False

counts = []
means = []
stds = []
medians = []
ses = []
limits = []
values = {}


opts, args = getopt.getopt(
    sys.argv[1:],
    "i:f:",
    ["in=","input=","field=","all","count","mean","std","se","median","limits","limit","minmax","max","min","sep=","with_title","title_diff_line", "title"],
)

for op, value in opts:
    if op == "-i" or op == "--in" or op == "--input":
        inputs.append(value)
    elif op == "-f" or op == '--field':
        for i in value.split(','):
            fields.append(int(i)-1)
    elif op == "--all":
        is_all = True
    elif op == "--count":
        is_count = True
    elif op == "--mean":
        is_mean = True
    elif op == "--std":
        is_std = True
    elif op == "--se":
        is_se = True
    elif op == "--median":
        is_median = True
    elif op == "--limits" or op == "--limit" or op == "--minmax":
        is_limits = True
    elif op == "--max":
        is_max = True
    elif op == "--min":
        is_min = True
    elif op == "--sep":
        sep = value
    elif op == "--with_title" or op == "--title":
        is_with_title = True
    elif op == "--title_diff_line":
        is_title_diff_line = True
    else:
        raise "illegal params"


##################################################
output_values = partial(output_values, is_with_title=is_with_title, is_title_diff_line=is_title_diff_line)

for input in inputs:
    values = dict(values, **read_input(input, sep, values, fields))

for index in sorted(values.keys()):
    a = values[index]
    counts.append(len(a))
    means.append(np.mean(a))
    stds.append(np.std(a))
    medians.append(get_median(a))
    ses.append(np.std(a)/np.sqrt(len(a)))
    limits.append(','.join(map(lambda x: str(x), [min(a),max(a)])))

if is_all:
    is_count, is_mean, is_std, is_median, is_limits, is_min, is_max = True, True, True, True, True, True, True

if is_count:
    output_values(counts, 'count', )
if is_mean:
    output_values(means, 'mean', )
if is_std:
    output_values(stds, 'std', )
if is_se:
    output_values(ses, 'se', )
if is_median:
    output_values(medians, 'median', )
if is_limits:
    output_values(limits, 'minmax', )
if is_min:
    output_values(map(lambda x: x.split(',')[0], limits), 'min')
if is_max:
    output_values(map(lambda x: x.split(',')[1], limits), 'max')


