from pyspark import pipelines as dp
from pyspark.sql.functions import *

SOURCE_PATH="/Volumes/training/employee/my_files"

@dp.materialized_view(name="training.default.employee")
def emp_bronze():
    df = spark.read.format("delta").load(SOURCE_PATH)
    return df