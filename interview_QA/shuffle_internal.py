"""
You are running a Spark job with joins and aggregations.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("ShuffleInternal").getOrCreate()

#Sample Data
data = [("A",100),
        ("B",200),
        ("A",300),
        ("B",400)]

df = spark.createDataFrame(data,["category","amount"])

#Aggregation (causes shuffle)
agg_df = df.groupBy("category").agg(F.sum("amount").alias("Total_Amount"))

agg_df.show()