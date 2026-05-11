"""
How to Find Median Salary by Company in PySpark without Percentile Functions
Just came across a classic yet tricky PySpark question asked in a recent Data Engineering interview at Tiger Analytics:
"Find the median salary for each company using PySpark — without using built-in percentile functions."
This is a common but powerful test of your understanding of:
➡️ Window functions
➡️ Cumulative logic
➡️ Handling grouped data
➡️ SQL/PySpark problem-solving
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import *

#Define Schema
schema = StructType([StructField("Id",IntegerType(),nullable=False),
                     StructField("Company",StringType(),nullable=False),
                     StructField("Salary",IntegerType(),nullable=False)])


# Sample data
data = [
    (1, "A", 2341), (2, "A", 341), (3, "A", 15), (4, "A", 15314),
    (5, "A", 451), (6, "A", 513), (7, "B", 15), (8, "B", 1154),
    (9, "B", 1345), (10, "B", 1221), (11, "B", 234), (12, "C", 2345),
    (13, "C", 2645), (14, "C", 2645), (15, "C", 2652), (16, "C", 65)
]

spark = SparkSession.builder.appName("MedianSalary").getOrCreate()

df = spark.createDataFrame(data,schema)

df1 = df.groupBy("Company",'Salary').agg(F.count('*').alias('freq'))\
 .withColumn('rnk1',F.sum(F.col('freq')).over(Window.partitionBy(F.col('Company')).orderBy(F.col('Salary'))))\
.withColumn('rnk2',F.sum(F.col('freq')).over(Window.partitionBy(F.col('Company')).orderBy(F.desc(F.col('Salary')))))\
 .withColumn('total_freq',F.sum(F.col('freq')).over(Window.partitionBy(F.col('Company'))))

df1.filter((F.col('rnk1') >= F.col('total_freq')/2) &  (F.col('rnk2') >= (F.col('total_freq')/2)))\
 .groupBy('Company').agg(F.round(F.avg('Salary'),2).alias('Median_Salary')).show()