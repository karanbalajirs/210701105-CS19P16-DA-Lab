#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
# the mapper will get daily max temperature and group it by month. so output will be
# (month, daily_max_temperature)

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    
    # split the line into words
    words = line.split()
    
    # See the README hosted on the weather website which helps us understand how each
    # position represents a column
    month = line[10:12]
    daily_max = line[38:45]
    daily_max = daily_max.strip()
    
    # increase counters
    # write the results to STDOUT (standard output);
    # what we output here will go through the shuffle process and then
    # be the input for the Reduce step, i.e., the input for reducer.py
    #
    # tab-delimited; month and daily max temp
    print(f"{month}\t{daily_max}")
