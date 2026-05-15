from pyspark import pipelines as dp
from pyspark.sql import functions as F

@dp.materialized_view(name="training.default.emp_silver")
def emp_silver():
    df_bronze = spark.read.table("training.default.employee")
    df_silver = df_bronze.select(F.col("id").alias("employee_id"), F.col("name").alias("employee_name"), F.col("salary"), F.col("department"))
    return df_silver
