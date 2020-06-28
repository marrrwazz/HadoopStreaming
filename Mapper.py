#!/usr/bin/python

import sys

for line in sys.stdin:
        line = line.strip()
        line = line.split('|')
        lo_quantity = line[8]
        lo_revenue = line[12]
        lo_discount = line[11]
        newline = [lo_quantity,lo_revenue]
        if int(lo_discount) < 3:
                print "\t".join(newline)
