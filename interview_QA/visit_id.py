"""
👉 Problem Statement:
Write a solution to find the IDs of the users who visited without making any transactions 
and the number of times they made these types of visits.
Return the result table sorted in any order.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Visit").getOrCreate()

#️⃣ creating visits dataframe
visits_data = [(1,23),(2,9),(4,30),(5,54),(6,96),(7,54),(8,54)]
visits_cols = ("visit_id","customer_id")
visits_df = spark.createDataFrame(visits_data, visits_cols)

#️⃣ creating transactions dataframe
transaction_data = [(2,5,310),(3,5,300),(9,5,200),(12,1,910),(13,2,970)]
transaction_cols = ("transaction_id","visit_id","amount")
transaction_df = spark.createDataFrame(transaction_data, transaction_cols)

joined_df = visits_df.join(transaction_df,on="visit_id",how="left")

zero_transactions = joined_df.filter(F.col("transaction_id").isNull()) \
                             .groupBy("customer_id").agg(F.count("visit_id").alias("no_of_visit"))

zero_transactions.show()