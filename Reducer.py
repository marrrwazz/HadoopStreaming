#!/usr/bin/python
# coding: utf-8

import sys

curr_id = None
curr_sum = 0
Id = None

for line in sys.stdin:
        line = line.strip()
        cols = line.split()
        id = int(cols[0])

        if curr_id == id:
                curr_sum = float(cols[1]) + curr_sum
        else:
             	if curr_id:
                        newline = [str(curr_id),str(curr_sum)]
                        print "\t".join(newline)
                curr_id = id
                curr_sum = 0

if curr_id == id:
        newline = [str(curr_id),str(curr_sum)]
        print "\t".join(newline)
