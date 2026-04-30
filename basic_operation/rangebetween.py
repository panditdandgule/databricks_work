"""
rangeBetween is a method in PySpark’s Window API that lets you define 
a value-based range for a window function, rather than a fixed number of rows. 
It’s useful when you want aggregations to span a range of values in the ORDER BY column.

start: The lower boundary of the range (inclusive), relative to the current row’s ORDER BY value.

end: The upper boundary of the range (inclusive), relative to the current row’s ORDER BY value.

start and end can be:

Integer offsets (e.g., 0 = current row, -1 = one before, 5 = five after).

Special constants:

Window.currentRow = current row.

Window.unboundedPreceding = no lower bound.

Window.unboundedFollowing = no upper bound
"""

from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("RangeBetween").getOrCreate()

df = spark.createDataFrame([(1, "a"), (1, "a"), (2, "a"), (1, "b"), (2, "b"), (3, "b")], ["id", "category"])

#This sums id values from the current row to the next row in each partition, not just the next row in position 
window = Window.partitionBy("category").orderBy("id").rangeBetween(Window.currentRow, 1)
df = df.withColumn("sum", sum("id").over(window))
df.show()
