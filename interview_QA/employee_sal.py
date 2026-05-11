"""
You are given a dataset containing employee data with their department, year of joining, and monthly salary.
Each row contains the department name, the year of joining, and the monthly salary of an employee.

Your task is to:
->Calculate the average monthly salary for each department.
->Filter out departments with an average salary lower than 3000.
->Calculate the total salary paid by each department over all years.
->Sort the results by total salary paid in descending order.
"""

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,StructField,StringType,IntegerType

spark = SparkSession.builder.appName("EmpSalary").getOrCreate()

schema = StructType([StructField("department",StringType(),nullable=False),
                     StructField("year",StringType(),nullable=True),
                     StructField("salary",IntegerType(),nullable=True)])

data = [
 ("HR", "2020", 2500), 
 ("HR", "2021", 3200), 
 ("HR", "2022", 2800), 
 ("Engineering", "2020", 5000), 
 ("Engineering", "2021", 6000), 
 ("Engineering", "2022", 5500), 
 ("Marketing", "2020", 4000), 
 ("Marketing", "2021", 3500), 
 ("Marketing", "2022", 3300)
]

df = spark.createDataFrame(data,schema)

sal_avg_df = df.groupBy("department").agg(F.avg("salary").alias("Avg_Salary"))

filter_df = sal_avg_df.where(F.col("Avg_Salary")<3000)

total_df = df.groupBy("department").agg(F.sum("salary").alias("Total_Salary"))

final_df = total_df.orderBy(F.desc("Total_Salary"))