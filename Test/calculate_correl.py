#! /bin/env

from scipy.stats import pearsonr
from scipy.stats import spearmanr
import getopt
import sys
import re


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


##########################################################################
inputs = []
fields = []
field_sep = " "


opts, args = getopt.getopt(
    sys.argv[1:],
    'i:f:',
    ['in=', 'field=', 'sep=', 'field_sep=']
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


if not fields:
  if len(inputs) == 2:
    fields = [[0],[0]]
  elif len(inputs) == 1:
    fields = [[0,1]]


##########################################################################
values = read_input(inputs, fields, field_sep)

print pearsonr(values.values()[0], values.values()[1])
print spearmanr(values.values()[0], values.values()[1])


