"""
You are building a data pipline that loads data daily.
Instead of loading full data every time, your task is:
1)Load only new or updated records
2)Avoid duplicate processing
3)Improve performance
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("IncrementalLoad").getOrCreate()

#Existing Target Data(already processed)
target_data = [(1,"Vinesh","2024-01-01"),
               (2,"Arjun","2024-01-05")]

target_df = spark.createDataFrame(target_data,["id","name","last_updated"])

#Incoming source data
source_data = [(1,"Vinesh","2024-01-01"),
               (2,"Arjun","2024-02-01"),
               (3,"Kiran","2024-03-01")]

source_df = spark.createDataFrame(source_data,["id","name","last_updated"])

#Find max processed date
max_date = target_df.select(F.max("last_updated")).collect()[0][0]

#Filter only new/updated records
incremental_df =source_df.filter(F.col("last_updated")>max_date)

final_df = target_df.unionByName(incremental_df)

final_df.show(truncate=False)