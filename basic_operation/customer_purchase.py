"""
You are given an orders dataset containing information about customer purchases.
Each order can contain multiple items stored in a single column as an array.

"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.winodw import Window

spark = SparkSession.builder.appName("CustomerPurchase").getOrCreate()

data = [
    (1, "Aarav", ["mango", "banana", "guava"]),
    (2, "Priya", ["apple", "lychee"]),
    (3, "Rohan", ["papaya"])
]
columns = ["order_id", "customer", "items"]

df =spark.createDataFrame(data,columns)

df = df.withColumn("item",F.explode("items")).drop("items")

df = df.withColumn("item",F.initcap("item"))
