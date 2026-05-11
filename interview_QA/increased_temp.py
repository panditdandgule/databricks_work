'''
𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧:

You are given a dataset containing the daily temperature readings for multiple cities:

Task:

Write a PySpark program to find all days where the temperature increased compared to the previous day for the same city.
'''

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("IncreaseTemp").getOrCreate()

#𝐬𝐜𝐡𝐞𝐦𝐚 𝐚𝐧𝐝 𝐝𝐚𝐭𝐚𝐬𝐞𝐭

data = [
  ("Delhi", "2024-01-01", 15),
  ("Delhi", "2024-01-02", 18),
  ("Delhi", "2024-01-03", 20),
  ("Delhi", "2024-01-04", 19),
  ("Mumbai", "2024-01-01", 28),
  ("Mumbai", "2024-01-02", 27),
  ("Mumbai", "2024-01-03", 30),
]
columns = ["city", "date", "temperature"]

df = spark.createDataFrame(data,columns)

windowSpec = Window.partitionBy("city").orderBy("date")

df_with_prev = df.withColumn("prev_temp",F.lag("temperature").over(windowSpec))

#Caluculate the diffrence
df_with_diff = df_with_prev.withColumn("temp_diff",F.col("temperature")-F.col("prev_temp"))

#Filter where temperature increased
df_increased = df_with_diff.filter(F.col("temp_diff")>0)

df_increased.show(truncate=False)
