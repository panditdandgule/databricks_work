#How to calculate cumulative sum and rank in PySpark

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

data = [
  (1, "HR", 50000, "2022-01-01"),
  (2, "IT", 70000, "2021-06-15"),
  (3, "HR", 60000, "2023-03-10"),
  (4, "IT", 80000, "2020-12-01")
]

columns = ["employee_id", "department", "salary", "join_date"]

spark = SparkSession.builder.appName("Fractual_cumsum").getOrCreate()

df = spark.createDataFrame(data,schema=columns)

#Cumulative sum of salaries per department ordered by join_date
window_cumsum = Window.partitionBy("department").orderBy("join_date").rowsBetween(Window.unboundedPreceding,Window.currentRow)

df_cumsum = df.withColumn("total_running_salary",F.sum(F.col("salary")).over(window_cumsum))

windowSpec =  Window.partitionBy("department").orderBy(F.col("salary").desc())

df = df_cumsum.withColumn("dense_rank",F.dense_rank().over(windowSpec))

df.show(truncate=False)