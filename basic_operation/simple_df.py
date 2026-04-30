from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()

data =[("pandit",3000)]
schema = ("name","count")
df = spark.createDataFrame(data,schema)

df.show()