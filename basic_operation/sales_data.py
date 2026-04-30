"""
you are given the following DataFrame df_sales with columns:
store_id (string)
product_id (string)
date (string in format yyyy-MM-dd)
sales (integer)

1️⃣ Convert date to proper date type.
2️⃣ Find the total sales per product per month for each store.
3️⃣ Rank products within each store-month by total sales (highest first).
4️⃣ Keep only the top 2 products per store per month.
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import *

spark = SparkSession.builder.appName("Sales").getOrCreate()

#Sample Data

data = [("S1","P1","2024-01-15",100),
		("S1","P2","2024-01-20",200),
		("S1","P3","2024-01-25",150),
		("S1","P1","2024-02-05",300),
		("S1","P2","2024-02-10",100),
		("S2","P1","2024-01-15",500),
		("S2","P2","2024-01-18",400),]

columns = ["store_id","product_id","date","sales"]

df = spark.createDataFrame(data,columns)

df = df.withColumn("date",F.to_date(F.col("date"),"yyyy-MM-dd"))

df_monthly = df.withColumn("year",F.year(F.col("date"))).withColumn("month",F.month(F.col("date"))) \
                .groupBy("product_id","store_id","year","month").agg(F.sum("sales").alias("Total_Sales"))

windowSpec = Window.partitionBy("store_id","year","month").orderBy(F.desc("Total_Sales"))

df_ranked = df_monthly.withColumn("Rank",F.rank().over(windowSpec))

df_top2 = df_ranked.filter(F.col("Rank")<=2)

df_top2.show()