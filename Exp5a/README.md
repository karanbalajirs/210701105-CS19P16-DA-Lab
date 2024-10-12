# Exp5a: Design and test various schema models to optimize data storage and retrieval Using Hive.

## Aim
To Design and test various schema models to optimize data storage and retrieval Using Hbase.

## Procedure
#### Step 1: Start Hive

Open a terminal and start Hive by running:
```shell
hive
```
#### Step 2: Create a Database
Create a new database in Hive:
```mysql
CREATE DATABASE financials;
```
#### Step 3: Use the Database:
Switch to the newly created database:

```mysql
use financials;
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp5a/Screenshot%20from%202024-09-16%2016-49-25.png)

#### Step 4: Create a Table:
Create a simple table in your database:

```mysql
CREATE TABLE finance_table( id INT, name STRING );
```

#### Step 5: Load Sample Data:
You can insert sample data into the table:
```mysql
INSERT INTO finance_tableVALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
```

#### Step 6: Query Your Data

Use SQL-like queries to retrieve data from your table:

```mysql
CREATE VIEW myview AS SELECT name, id FROM finance_table;
```
#### Step 7: View the data:

To see the data in the view, you would need to query the view
```mysql
SELECT * FROM myview;
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp5a/Screenshot%20from%202024-09-16%2016-50-21.png)

#### Step 8: Describe a Table:
You can describe the structure of a table using the DESCRIBE command:
```mysql
DESCRIBE finance_table;
```

#### Step 9: Alter a Table:
You can alter the table structure by adding a new column:

```mysql
ALTER TABLE finance_table ADD COLUMNS (age INT);
```

#### Step 10: Quit Hive:
To exit the Hive CLI, simply type:

```mysql
quit;
```

## Result
Thus, the usage of various commands in Hive has been successfully completed.