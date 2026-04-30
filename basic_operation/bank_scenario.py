'''
You are working in a banking project.
You receive two datasets

1)Customers Data
2)Transaction Data

Your task:
Join both datasets
Find total transaction amount per customer
Identify customers with transactions > 300
'''

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("BankProject").getOrCreate()

#Customers Data
customers_data = [(1,"Vinesh"),
                  (2,"Arjun"),
                  (3,"Kiran")]

customers_df = spark.createDataFrame(customers_data,["cust_id","name"])

#transaction data
transaction_data =[(101,1,200),
                   (102,2,400),
                   (103,1,150),
                   (104,3,100),
                   (105,2,200)]

transaction_df = spark.createDataFrame(transaction_data,["txn_id","cust_id","amount"])

joined_df = customers_df.join(transaction_df,on="cust_id",how="inner")

total_df = joined_df.groupBy("cust_id").agg(F.sum("amount").alias("total_amount"))

result_df = total_df.where(F.col("total_amount")>300)

result_df.show(truncate=False)