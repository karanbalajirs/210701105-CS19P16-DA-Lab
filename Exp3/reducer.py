#!/usr/bin/env python
from operator import itemgetter
import sys

# Reducer will get the input from stdin which will be a collection of key-value pairs
# (Key=month, Value=daily_max_temperature)
# Reducer logic: will get all the daily max temperatures for a month and find the max temperature for the month
# Shuffle will ensure that keys are sorted (month)

current_month = None
current_max = float('-inf')  # Initialize to a very small number to handle all possible temperatures
month = None

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    
    # Parse the input we got from mapper.py
    month, daily_max = line.split('\t', 1)

    # Convert daily_max (currently a string) to float
    try:
        daily_max = float(daily_max)
    except ValueError:
        # daily_max was not a number, so silently ignore/discard this line
        continue
    
    # This IF-switch only works because Hadoop shuffle process sorts map output by key (here: month)
    # before it is passed to the reducer
    if current_month == month:
        if daily_max > current_max:
            current_max = daily_max
    else:
        if current_month:
            # Write result to STDOUT
            print('%s\t%s' % (current_month, current_max))
        current_max = daily_max
        current_month = month

# Output of the last month
if current_month == month:
    print('%s\t%s' % (current_month, current_max))
