-- Load the data from HDFS
data = LOAD '/exp4/sample.txt' USING PigStorage(',') AS (id:int,name:chararray);

-- Dump the data to check if it was loaded correctly
DUMP data;
