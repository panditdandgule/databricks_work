"""
rangeBetween(start, end)

Defines the frame boundaries, from start (inclusive) to end (inclusive).

Both start and end are relative from the current row. For example, “0” means “current row”, while “-1” means one off before the current row, and “5” means the five off after the current row.

Parameters:

start – boundary start, inclusive. The frame is unbounded if this is -sys.maxsize (or lower).
end – boundary end, inclusive. The frame is unbounded if this is sys.maxsize (or higher). New in version 1.4.

rowsBetween(start, end)

Defines the frame boundaries, from start (inclusive) to end (inclusive).

Both start and end are relative positions from the current row. For example, “0” means “current row”, while “-1” means the row before the current row, and “5” means the fifth row after the current row.

Parameters:

start – boundary start, inclusive. The frame is unbounded if this is -sys.maxsize (or lower).
end – boundary end, inclusive. The frame is unbounded if this is sys.maxsize (or higher). New in version 1.4.
ROWS BETWEEN doesn't care about the exact values. It cares only about the order of rows, and takes fixed number of preceding and following rows when computing frame.
RANGE BETWEEN considers values when computing frame.
Let's use an example using two window definitions:

ORDER BY x ROWS BETWEEN 2  PRECEDING AND CURRENT ROW
ORDER BY x RANGE BETWEEN 2  PRECEDING AND CURRENT ROW
and data as
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder.appName("WindowExample").getOrCreate()

# Sample data
data = [
    (1, 100),
    (2, 200),
    (3, 300),
    (4, 400),
    (5, 500)
]
df = spark.createDataFrame(data, ["id", "value"])

# Window ordered by 'id'
# ROWS BETWEEN: 1 row before to 1 row after
rows_window = Window.orderBy("id").rowsBetween(-1, 1)

# RANGE BETWEEN: values within 1 unit of 'id'
range_window = Window.orderBy("id").rangeBetween(-1, 1)

# Apply aggregations
result = df.select(
    "id",
    "value",
    F.sum("value").over(rows_window).alias("sum_rowsBetween"),
    F.sum("value").over(range_window).alias("sum_rangeBetween")
)

result.show()


