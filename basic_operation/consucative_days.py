"""
You work for a large Indian IT services company like TCS or Infosys. You’re given daily attendance logs.
Your task is to:
Identify streaks of consecutive days an employee was present.

"""

from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,StructField,StringType,IntegerType

spark = SparkSession.builder.appName("ConsucativeDays").getOrCreate()

schema = StructType([StructField("emp_id",StringType(),nullable=False),
                     StructField("login_date",StringType(),nullable=False)])
data = [
  ("E001", "2024-06-01"),
  ("E001", "2024-06-02"),
  ("E001", "2024-06-03"),
  ("E001", "2024-06-05"),
  ("E002", "2024-06-01"),
  ("E002", "2024-06-03"),
  ("E002", "2024-06-04")
]

df = spark.createDataFrame(data,schema)

df = df.withColumn("login_date",F.to_date("login_date"))

windowSpec  = Window.partitionBy("emp_id").orderBy("login_date")

df = df.withColumn("prev_date",F.lag("login_date").over(windowSpec))

df = df.withColumn("gap",F.datediff("login_date","prev_date"))

df = df.withColumn("is_new_streak",(F.col("gap")!=1).cast("int"))

df = df.withColumn("streak_id",F.sum("is_new_streak").over(windowSpec.rowsBetween(Window.unboundedPreceding,0)))

df = df.groupBy("emp_id","streak_id") \
        .agg(F.min("login_date").alias("start_date"),
             F.max("login_date").alias("end_date"))
df = df.withColumn("days_present",(F.datediff("start_date","end_date")+1)).orderBy("emp_id","start_date")