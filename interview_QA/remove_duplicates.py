"""
You are working in a data pipeline where duplicate customer records are coming from multiple sources.

Your Task:
1)Remove duplicate records
2)Keep only the latest record per customer based on timestamp
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("RemoveDuplicates").getOrCreate()

#Sampel Data
data = [(1,"Vinesh","2024-01-01"),
        (1,"Vinesh","2024-02-01"),
        (2,"Arjun","2024-01-15"),
        (2,"Arjun","2024-03-01"),
        (3,"Kiran","2024-02-10")]

df = spark.createDataFrame(data,["cust_id","name","update_date"])

df_clean =df.dropDuplicates(subset=["cust_id","name","update_date"])

windowSpec = Window.partitionBy("cust_id").orderBy(F.col("update_date").desc())

latest_record =df_clean.withColumn("row_number",F.row_number().over(windowSpec))

final_result = latest_record.where(F.col("row_number")==1).drop("row_number")

final_result.show()
