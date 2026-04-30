"""
Problem Statement:
You are given a user activity log for an Indian mobile app. Each row contains a user_id and 
a timestamp representing when the user performed an action (e.g., opened the app, clicked, etc.).
Create a PySpark solution to group user activity into sessions, 
where a session is defined as a sequence of actions from the same user with no more than 30 minutes 
between consecutive events.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("UserSession").getOrCreate()

data = [
  ("U001", "2024-01-01 10:00:00"),
  ("U001", "2024-01-01 10:10:00"),
  ("U001", "2024-01-01 11:00:00"),
  ("U001", "2024-01-01 11:05:00"),
  ("U002", "2024-01-01 12:00:00"),
  ("U002", "2024-01-01 13:00:00"),
  ("U003", "2024-01-01 09:00:00"),
  ("U003", "2024-01-01 09:35:00"),
]

#Create DataFrame
df = spark.createDataFrame(data, ["user_id", "timestamp"])

windowSpec = Window.partitionBy("user_id").orderBy("timestamp")

df = df.withColumn("prev_timestamp",F.lag("timestamp").over(windowSpec))

df = df.withColumn("diff_sec",(F.unix_timestamp("timestamp")-F.unix_timestamp("prev_timestamp")))

df = df.withColumn("new_session",F.when((F.col("diff_sec")>1000) | F.col("diff_sec").isNull(),1).otherwise(0))

df = df.withColumn("session_id",F.sum("new_session").over(windowSpec))

session_df = df.groupBy("user_id","session_id").agg(F.min("timestamp").alias("session_start"),
                                                    F.max("timestamp").alias("session_end"),
                                                    F.count("*").alias("activity_count")).orderBy("user_id","session_id")

session_df.show(truncate=False)