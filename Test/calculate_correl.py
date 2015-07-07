#! /bin/env

from scipy.stats import pearsonr
from scipy.stats import spearmanr
import getopt
import sys
import re


##########################################################################
inputs = []
fields = []
field_sep = " "

is_pearson = True
is_spearman = True
is_only_p_value = False
is_with_title = False


##########################################################################
def read_input(inputs, fields, field_sep):
    values = {}
    for index_1, input in enumerate(inputs):
        fh = open(input, 'r')
        for line in fh.readlines():
            line = line.rstrip('\n\r')
            line_array = line.split("\t")
            for index_2, field in enumerate(fields[index_1]):
                key = '-'.join([str(index_1),str(index_2)])
                if not key in values:
                    values[key] = []
                item = float(line_array[field])
                values[key].append(item)
        fh.close()
    return(values)


def get_correl_coeffieicnt(method, values_0, values_1, is_only_p_value):
    result = None
    if method == "pearson":
        result = pearsonr(values_0, values_1)
    elif method == "spearman":
        result = spearmanr(values_0, values_1)
    else:
        raise "Unknown method for calculating correlation coefficients. Exiting ......"

    if is_only_p_value:
        result = result[1]
    return(result)
        

##########################################################################
opts, args = getopt.getopt(
    sys.argv[1:],
    'i:f:',
    ['in=', 'field=', 'sep=', 'field_sep=', "no_pearson", "no_spearman", "only_p_value", "only_p-value", "with_title"]
)


for opt, value in opts:
    if opt == "-i" or opt == "--in":
        for i in value.split(','):
            inputs.append(i)
    elif opt == '-f' or opt == '--field':
        for index, i in enumerate(value.split(';')):
            fields.append([])
            for j in i.split(','):
                fields[index].append(int(j)-1)
    elif opt == '-f' or opt == '--field':
        field_sep = value
    elif opt == "--no_pearson":
        is_pearson = False
    elif opt == "--no_spearman":
        is_spearman = False
    elif opt == "--only_p_value" or opt == "--only_p-value":
        is_only_p_value = True
    elif opt == "--with_title":
        is_with_title = True


if not fields:
    if len(inputs) == 2:
        fields = [[0],[0]]
    elif len(inputs) == 1:
        fields = [[0,1]]


##########################################################################
values = read_input(inputs, fields, field_sep)

if is_pearson:
    if is_with_title:
        print "pearson"+"\t",
    print get_correl_coeffieicnt('pearson', values.values()[0], values.values()[1], is_only_p_value)
if is_spearman:
    if is_with_title:
        print "spearman"+"\t",
    print get_correl_coeffieicnt('spearman', values.values()[0], values.values()[1], is_only_p_value)
    


