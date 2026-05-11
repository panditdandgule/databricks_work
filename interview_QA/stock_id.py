"""
You are given a dataset of stock prices with the following columns:

- stock_id: Unique identifier for the stock.
- date: The date of the stock price.
- price: The price of the stock on the given date.

Your task is to calculate the 3-day rolling average of the stock price (rolling_avg) for each stock (stock_id) using a sliding window, ensuring the results are partitioned by stock_id and ordered by date.

"""

from pypsark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("StockPrice").getOrCreate()

data = [ ("A", "2023-01-01", 100), ("A", "2023-01-02", 105), 
("A", "2023-01-03", 110), ("A", "2023-01-04", 120), 
("B", "2023-01-01", 50), ("B", "2023-01-02", 55), 
("B", "2023-01-03", 60), ("B", "2023-01-04", 65), ] 

# Define schema 
columns = ["stock_id", "date", "price"] 

df = spark.createDataFrame(data,columns)

windowSpec = Window.partitionBy("stock_id").orderBy("date").rowsBetween(-2,0)

df = df.withColumn("rolling_avg",F.avg("price").over(windowSpec))

df.show()