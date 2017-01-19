#! /bin/python

import csv
import sys
from itertools import *

with open('israel.csv', 'rt') as f:
	#reader=csv.reader(f)
	#for row in reader:
		#print(' '.join(row))
	it = islice(f, 0, min(0+sys.maxsize, sys.maxsize))
	#for row in csv.reader(it):
		#print(' '.join(row))
	lst = {int(row[0]): int(row[0]) for row in csv.reader(it)}
