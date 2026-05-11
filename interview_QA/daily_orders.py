'''
Scenario1: You are working as a Data Engineer in an e-commerce company:
You receive daily orders data and need to:
1)Filter only completed orders
2)Calculate total revenue per customer
3)identify top customers.
'''

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

#Create a spark session
spark = SparkSession.builder.appName("DailyOrders").getOrCreate()

#Sample Data
data = [(1,"cust1",100,"completed"),
        (2,"cust2",200,"completed"),
        (3,"cust1",300,"pending"),
        (4,"cust3",150,"completed"),
        (5,"cust2",250,"completed")]

columns = ["order_id","customer_id","amount","status"]

df = spark.createDataFrame(data,columns)

completed_order = df.filter(F.col("status").contains("completed"))

revenue_df = completed_order.groupBy("customer_id").agg(F.sum("amount").alias("Total_Revenue"))

top_customers = revenue_df.orderBy(F.col("Total_Revenue").desc())

top_customers.show(truncate=False)