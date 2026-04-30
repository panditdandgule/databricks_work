"""
You are given a user activity log containing login events for a mobile application. Each row in the dataset represents a user's login on a specific date.
Write a PySpark solution to calculate:
Day 1 Retention: Users who returned 1 day after signup
Day 7 Retention: Users who returned 7 days after signup
Day 30 Retention: Users who returned 30 days after signup
Assume each user’s first login date is their signup date. Provide your solution using sample data from Indian users.

"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("UserSignup").getOrCreate()

data = [
  ("U001", "2024-01-01"),
  ("U001", "2024-01-02"), # Day 1
  ("U001", "2024-01-08"), # Day 7
  ("U001", "2024-01-31"), # Day 30
  ("U002", "2024-01-01"),
  ("U002", "2024-01-03"),
  ("U003", "2024-01-02"),
  ("U003", "2024-01-03"), # Day 1
  ("U003", "2024-02-01"), # Day 30
]

df = spark.createDataFrame(data,["user_id","login_date"])

df = df.withColumn("login_date",F.col("login_date").cast("date"))

signup_df = df.groupBy("user_id").agg(F.min("login_date").alias("signup_date"))

df = df.join(signup_df,on="user_id",how="inner")

date_diff = df.withColumn("date_diff",F.datediff(F.col("login_date"),F.col("signup_date")))

retention_df = date_diff.filter(F.col("date_diff").isin(1,7,30))

