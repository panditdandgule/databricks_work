from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(name="training.default.emp_gold")

def emp_gold():
    df_silver = spark.read.table("training.default.emp_silver")
    df_silver = df_silver.withColumn("salary", F.col("salary") * 1.1)
    return df_silver.withColumn("salary", F.round(F.col("salary"), 2))
