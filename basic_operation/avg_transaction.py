"""
You have a dataset of transactions with the following fields:
transaction_id (integer): Unique ID for each transaction.
user_id (integer): ID of the user performing the transaction.
transaction_amount (float): Amount of the transaction.
transaction_date (string): Date of the transaction in yyyy-MM-dd format.
From this dataset, perform the following operations:
Identify users who have made transactions on at least 3 different dates.
For these users, calculate their average transaction amount.
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,StructField,IntegerType,StringType,FloatType

spark = SparkSession.builder.appName("TransactionAmount").getOrCreate()

schema = StructType([StructField("transaction_id",IntegerType(),nullable=False),
                     StructField("user_id",IntegerType(),nullable=False),
                     StructField("transaction_amount",FloatType(),nullable=False),
                     StructField("transaction_date",StringType(),nullable=False)])

data = [
 (1, 101, 500.0, "2024-01-01"), 
 (2, 102, 200.0, "2024-01-02"), 
 (3, 101, 300.0, "2024-01-03"), 
 (4, 103, 100.0, "2024-01-04"), 
 (5, 102, 400.0, "2024-01-05"), 
 (6, 103, 600.0, "2024-01-06"), 
 (7, 101, 200.0, "2024-01-07"),
]
#columns = ["transaction_id", "user_id", "transaction_amount", "transaction_date"]

df = spark.createDataFrame(data,schema)

#count distinct date per user
user_df =  df.groupBy("user_id").agg(F.countDistinct("transaction_date").alias("distinct_transaction_count"))

#Filter user atleast 3 transaction
filter_user = user_df.filter(F.col("distinct_transaction_count")>=3)

final_result = df.join(filter_user,on="user_id",how="inner")

final_result = final_result.groupBy("user_id").agg(F.avg("transaction_amount").alias("avg_transaction_amount"))


