
# EXP 4: Create UDF in PIG

## Aim 
To create User Define Function in Apache Pig and execute it on map reduce.

## Procedure
#### Create a sample text file

```shell
nano sample.txt
```
Paste the below content to sample.txt

```shell
1,John
2,Jane
3,Joe
4,Emma
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp4/Images/Screenshot%20from%202024-09-16%2016-40-44.png)

```shell
hadoop fs -put sample.txt /exp4
```

#### Create PIG File
```shell
nano demo_pig.pig
```

**paste the below the content to demo_pig.pig**

```piglatin
-- Load the data from HDFS
data = LOAD '/exp4/sample.txt' USING PigStorage(',') AS (id:int,name:chararray);

-- Dump the data to check if it was loaded correctly
DUMP data;
```

**Run the above file**

```shell
pig demo_pig.pig
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp4/Images/Screenshot%20from%202024-09-16%2016-42-38.png)


#### Create udf file an save as uppercase.py

**uppercase.py**

```python
def uppercase(text):
	return text.upper()
if __name__ == "__main__":
	import sys
	for line in sys.stdin:
		line = line.strip()
		result = uppercase(line)
		print(result)
```

#### Create the exp4 folder on hadoop

```shell
hadoop fs -mkdir /exp4
```

#### Put the upppercase.py in to the above folder

```shell
hdfs dfs -put uppercase.py /exp4
```

```shell
nano udf_example.pig
```

**Copy and paste the below content on udf_example.pig**

```shell
REGISTER 'hdfs:///exp4/uppercase.py' USING jython AS udf;
data = LOAD 'hdfs:///exp4/sample.txt' AS (text:chararray);
uppercased_data = FOREACH data GENERATE udf.uppercase(text) AS uppercase_text;
STORE uppercased_data INTO 'hdfs:///exp4/pig_output_data';
```

**Place sample.txt file on hadoop**

```shell
hadoop fs -put sample.txt /exp4
```

**To Run the pig file**

```shell
pig -f udf_example.pig
```

#### Output

To view the output.

```shell
hdfs dfs -cat /exp4/pig_output_data/*
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp4/Images/Screenshot%20from%202024-09-16%2016-43-05.png)

## Result

Thus the program is executed successfully.
