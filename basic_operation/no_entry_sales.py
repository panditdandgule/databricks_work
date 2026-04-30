"""
Write a PySpark script to find all products from the products table that were never sold, i.e., 
there is no entry for them in the sales table.

You are given two DataFrames:
products:
 Columns → product_id, product_name
sales:
 Columns → sale_id, product_id, quantity, sale_date
"""
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


spark= SparkSession.builder.appName("SalesData").getOrCreate()

products_data = [
  (1, "Apple"),
  (2, "Banana"),
  (3, "Carrot"),
  (4, "Dates")
]

prod_columns=["product_id","product_name"]

sales_data = [
  (101, 1, 10, "2021-01-01"),
  (102, 2, 5, "2021-01-02"),
  (103, 1, 8, "2021-01-03")
]

sales_columns=["sale_id","product_id","quantity","sale_date"]

prod_df =spark.createDataFrame(products_data,prod_columns)

sales_df = spark.createDataFrame(sales_data,sales_columns)

joined_df = prod_df.join(sales_df,on="product_id",how="left_anti")

