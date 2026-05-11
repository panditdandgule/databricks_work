'''
Stumbled upon a classic (yet tricky!) PySpark problem in a recent DE interview prep — and wanted to share the solution for fellow data engineers.
Problem:
For each user, find the number of days between their first and last post within a year.
'''

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import StructType,StructField,StringType,IntegerType

# Sample data
data = [
('151652', 599415, '2025-07-10 12:00:00', 'Need a hug'),
('661093', 624356, '2025-07-29 13:00:00', 'Bed. Class 8-12. Work 12-3. Gym 3-5 or 6.'),
('004239', 784254, '2025-07-04 11:00:00', 'Happy 4th of July!'),
('661093', 442560, '2025-07-08 14:00:00', 'Just going to clean & organize my room.'),
('151652', 111766, '2025-07-12 19:00:00', 'Its Cheat Day!')
]

schema = StructType([
StructField('user_id', StringType()),
StructField('post_id', IntegerType()),
StructField('post_date', StringType()),
StructField('post_content', StringType()),
])

spark = SparkSession.builder.appName("DiffpostDate").getOrCreate()

df = spark.createDataFrame(data, schema)

# Convert string to timestamp
df = df.withColumn('post_date', F.to_timestamp(F.col('post_date'), 'yyyy-MM-dd HH:mm:ss'))

df.withColumn('rnk1',F.rank().over(Window.partitionBy(F.col('user_id')).orderBy(F.col('post_date'))))\
  .withColumn('rnk2',F.rank().over(Window.partitionBy(F.col('user_id')).orderBy((F.col('post_date').desc()))))\
  .groupby('user_id')\
  .agg(
    max(F.when(F.col('rnk1')==1,F.col('post_date'))).alias('first_post_date'),
    max(F.when(F.col('rnk2')==1,F.col('post_date'))).alias('last_post_date')
    )\
  .withColumn('no_of_days',F.date_diff('last_post_date','first_post_date')).show()