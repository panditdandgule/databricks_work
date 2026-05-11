"""
You’re working as a Data Engineer for a power distribution company in India. 
Customers are billed daily, but due to technical issues, 
some records are missing in the billing_logs table. 
Management wants to find out the missing billing dates for each customer.

Identify continuous date gaps in billing logs for each customer between their first and last billing date.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("BillingIssue").getOrCreate()

data = [
  ("C001", "2024-01-01"),
  ("C001", "2024-01-02"),
  ("C001", "2024-01-04"),
  ("C001", "2024-01-06"),
  ("C002", "2024-01-03"),
  ("C002", "2024-01-05"),
]

df = spark.createDataFrame(data, ["customer_id", "billing_date"])

df = df.withColumn("billing_date",F.to_date("billing_date"))

df = df.groupBy("customer_id").agg(F.min("billing_date").alias("start_date"),
                                   F.max("billing_date").alias("end_date"))

df = df.withColumn("date",F.explode(F.sequence("start_date","end_date"))).drop("start_date","end_date")

missing_date_df = df.withColumnRenamed("date","missing_date")
