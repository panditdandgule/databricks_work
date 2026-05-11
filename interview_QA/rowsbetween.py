"""
In PySpark,
rowsBetween(Window.unboundedPreceding, Window.currentRow) 
is used in window functions to define a frame that starts from the very first row in the partition and 
ends at the current row.

This is commonly used for running totals, cumulative counts, or progressive aggregations.

Key Points:
Window.unboundedPreceding → Start from the first row in the partition.
Window.currentRow → End at the current row.
This frame includes all rows up to and including the current row.
Useful for cumulative aggregations.

Example: Running Total in PySpark
"""
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import col, sum as _sum

# Create Spark session
spark = SparkSession.builder.appName("RowsBetweenExample").getOrCreate()

# Sample data
data = [
    ("A", 100),
    ("A", 200),
    ("A", 300),
    ("B", 50),
    ("B", 150)
]
df = spark.createDataFrame(data, ["category", "value"])

# Define window specification
# Partition by category, order by value
# Frame: from first row in partition to current row

windowSpec = Window.partitionBy("category").orderBy("value").rowsBetween(Window.unboundedPreceding,Window.currentRow)

#calculate running total
df_with_running_total = df.withColumn("running_total",_sum(col("value")).over(windowSpec))

