'''
Question:
You are given an employee dataset from an Indian IT company. 
Each employee can have multiple records based on updates to their information.
 The dataset has the following columns:
emp_id: Unique employee ID
emp_name: Employee name
update_date: Date on which employee record was updated
'''

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("RemoveDuplicates").getOrCreate()

# Sample Indian employee data
data = [
  (101, "Rajesh Kumar", "2023-01-01"),
  (101, "Rajesh Kumar", "2023-05-12"),
  (102, "Anjali Mehta", "2023-02-15"),
  (103, "Rakesh Yadav", "2023-01-20"),
  (103, "Rakesh Yadav", "2023-06-30")
]

# Create DataFrame
columns = ["emp_id", "emp_name", "update_date"]

df = spark.createDataFrame(data,columns)

windowSpec = Window.partitionBy("emp_id").orderBy(F.col("update_date").desc())


df =  df.withColumn("row_number",F.row_number().over(windowSpec))

df = df.filter(F.col("row_number")==1)

df.show()