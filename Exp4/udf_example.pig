REGISTER 'hdfs:///exp4/uppercase.py' USING jython AS udf;
data = LOAD 'hdfs:///exp4/sample.txt' AS (text:chararray);
uppercased_data = FOREACH data GENERATE udf.uppercase(text) AS uppercase_text;
STORE uppercased_data INTO 'hdfs:///exp4/pig_output_data';
