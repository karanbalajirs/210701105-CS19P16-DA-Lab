
# EXP 3: Map Reduce program to process a weather dataset.

## Aim
To implement MapReduce program to process a weather dataset.

## Procedure
#### Step 1: Create Data File:
Create a file named *word_count_data.txt* and populate it with text data that you wish to
analyse.

Login with your hadoop user.

**Download the dataset(Weather dataset)**
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp3/Images/Screenshot%20from%202024-09-16%2016-39-07.png)

#### Step 2: Mapper Logic - mapper.py:

Create a file named *mapper.py* to implement the logic for the mapper. The mapper
will read input data from *STDIN*, split lines into words, and output each word with its count.

```shell
nano mapper.py
```
**mapper.py**
```python
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
```

#### Step 3: Reducer Logic - reducer.py:

Create a file named "reducer.py" to implement the logic for the reducer. The reducer
will aggregate the occurrences of each word and generate the final output.

```shell
nano reducer.py
```
**reducer.py**

```python
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
```

#### Step 4: Prepare Hadoop Environment:

Start the Hadoop daemons and create a directory in HDFS to store your data.

```shell
start-all.sh
```
#### Step 5: Make Python Files Executable:

Give executable permissions to your mapper.py and reducer.py files.

```shell
chmod 777 mapper.py reducer.py
```

#### Step 6: Run the program using Hadoop Streaming:

Download the latest hadoop-streaming jar file and place it in a location you can easily
access.
Then run the program using Hadoop Streaming

```shell
hadoop fs -mkdir -p /weatherdata
```
```shell
hadoop fs -copyFromLocal /home/s/Downloads/dataset.txt /weatherdata
```
```shell
hdfs dfs -ls /weatherdata
```
```shell
hadoop jar /home/sx/hadoop-3.2.3/share/hadoop/tools/lib/hadoop-streaming-3.2.3.jar \
 -input /weatherdata/dataset.txt \
 -output /weatherdata/output \
 -file "/home/sx/Downloads/mapper.py" \
 -mapper "python3 mapper.py" \
 -file "/home/sx/Downloads/reducer.py" \
 -reducer "python3 reducer.py"
```
```shell
hdfs dfs -text /weatherdata/output/* > /home/sx/Downloads/outputfile.txt
```

#### Step 7: Check Output:

Check the output of the program in the specified HDFS output directory.

```shell
hdfs dfs -text /weatherdata/output/* > /home/sx/Downloads/output/
part-00000
```

After copy and paste the above output in your local file give the below command to
remove the directory from hdfs :

```shell
hadoop fs -rm -r /weatherdata/output
```
## Result

Thus, the program for weather dataset using Map Reduce has been executed successfully.