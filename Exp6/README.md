# Exp 6: Handling JSON data using HDFS and Python

## Aim
To handling JSON data using HDFS and Python.

## Procedure

#### Step 1: Create emp.json file

```shell
nano emp.json
```
Paste the below to the file.

```json
[
    {"name": "John Doe", "age": 30, "department": "HR", "salary": 50000},
    {"name": "Jane Smith", "age": 25, "department": "IT", "salary": 60000},
    {"name": "Alice Johnson", "age": 35, "department": "Finance", "salary": 70000},
    {"name": "Bob Brown", "age": 28, "department": "Marketing", "salary": 55000},
    {"name": "Charlie Black", "age": 45, "department": "IT", "salary": 80000}
]
```

#### Step 2: Execute jq:

Use the below command to verify the JSON Parsing.

```shell
jq . emp.json
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp6/Images/Screenshot%20from%202024-10-13%2006-46-37.png)

#### Step 3: pip install pandas and HDFS

Use the below command to install pandas and HDFS.

```shell
pip install pandas hdfs
```

![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp6/Images/Screenshot%20from%202024-10-13%2006-34-01.png)

#### Step 4: Create process_data.py

```shell
nano process_data.py
```
Paste the below into the file.

```python
from hdfs import InsecureClient
import pandas as pd
import json

# Connect to HDFS
hdfs_client = InsecureClient('http://localhost:9870', user='hdfs')

# Read JSON data from HDFS
try:
    with hdfs_client.read('/exp6/emp.json', encoding='utf-8') as reader:
        json_data = reader.read()  # Read the raw data as a string
        if not json_data.strip():  # Check if data is empty
            raise ValueError("The JSON file is empty.")
        print(f"Raw JSON Data: {json_data[:1000]}")  # Print first 1000 characters for debugging
        data = json.loads(json_data)  # Load the JSON data
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
    exit(1)
except Exception as e:
    print(f"Error reading or parsing JSON data: {e}")
    exit(1)

# Convert JSON data to DataFrame
try:
    df = pd.DataFrame(data)
except ValueError as e:
    print(f"Error converting JSON data to DataFrame: {e}")
    exit(1)

# Projection: Select only 'name' and 'salary' columns
projected_df = df[['name', 'salary']]

# Aggregation: Calculate total salary
total_salary = df['salary'].sum()

# Count: Number of employees earning more than 50000
high_earners_count = df[df['salary'] > 50000].shape[0]

# Limit: Get the top 5 highest earners
top_5_earners = df.nlargest(5, 'salary')

# Skip: Skip the first 2 employees
skipped_df = df.iloc[2:]

# Remove: Remove employees from a specific department
filtered_df = df[df['department'] != 'IT']

# Save the filtered result back to HDFS
filtered_json = filtered_df.to_json(orient='records')
try:
    with hdfs_client.write('/exp6/filtered_employees.json', encoding='utf-8', overwrite=True) as writer:
        writer.write(filtered_json)
    print("Filtered JSON file saved successfully.")
except Exception as e:
    print(f"Error saving filtered JSON data: {e}")
    exit(1)

# Print results
print(f"Projection: Select only name and salary columns")
print(f"{projected_df}")

print(f"Aggregation: Calculate total salary")
print(f"Total Salary: {total_salary}\n")

print(f"# Count: Number of employees earning more than 50000")
print(f"Number of High Earners (>50000): {high_earners_count}\n")

print(f"Limit: Top 5 highest salaries")
print(f"Top 5 Earners: \n{top_5_earners}\n")

print(f"Skipped DataFrame (First 2 rows skipped): \n{skipped_df}\n")
print(f"Filtered DataFrame (IT department removed): \n{filtered_df}")
```

#### Step 5: Run process_data.py

You can run the file after inserting the emp.json into the hdfs.

```shell
python process_data.py
```
![Output](https://github.com/karanbalajirs/210701105-CS19P16-DA-Lab/blob/master/Exp6/Images/Screenshot%20from%202024-10-13%2006-42-28.png)

## Result 

Thus handling JSON data using HDFS and Python is done successfully.


