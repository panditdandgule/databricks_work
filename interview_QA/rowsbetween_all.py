"""
https://stackoverflow.com/questions/72607940/how-to-use-unboundedpreceding-unboundedfollowing-and-currentrow-in-rowsbetween

How to use unboundedPreceding, unboundedFollowing and currentRow in rowsBetween in PySpark

Window.unboundedPreceding, 
Window.unboundedFollowing, and 
Window.currentRow objects as start and end arguments.

So as expected it looked at each price from top to bottom one by one and populated the 
max value it got this behaviour is known as 
start = Window.unboundedPreceding to end = Window.currentRow

Now changing rows between values to 
start = Window.unboundedPreceding to end = Window.unboundedFollowing we will get as below:

Now as you can see in the same window it's looking downwards in all values for a max instead of limiting it to the current row.

Now third will be start = Window.currentRow and end = Window.unboundedFollowing

"""
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("rowsbetween").getOrCreate()

dfw = (
    spark
    .createDataFrame(
        [
            ("abc", 1, 100),
            ("abc", 2, 200),
            ("abc", 3, 300),
            ("abc", 4, 200),
            ("abc", 5, 100),
        ],
        "name string,id int,price int",
    )
)

dfw=dfw.withColumn("rm",F.max("price").over(Window.partitionBy("name").orderBy("id")))


dfw=dfw.withColumn("rm1",F.max("price").over(Window.partitionBy("name").orderBy("id").rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing)))

dfw=dfw.withColumn("rm2",F.max("price").over(Window.partitionBy("name").orderBy("id").rowsBetween(Window.currentRow,Window.unboundedFollowing)))

"""
Now over this data let's try to find of running max i.e max for each row:

(
    dfw
    .withColumn(
        "rm",
        F.max("price").over(Window.partitionBy("name").orderBy("id"))
    )
    .show()
)

#output
+----+---+-----+---+
|name| id|price| rm|
+----+---+-----+---+
| abc|  1|  100|100|
| abc|  2|  200|200|
| abc|  3|  300|300|
| abc|  4|  200|300|
| abc|  5|  100|300|
+----+---+-----+---+
So as expected it looked at each price from top to bottom one by one and populated the max value it got this behaviour is known as start = Window.unboundedPreceding to end = Window.currentRow

Now changing rows between values to start = Window.unboundedPreceding to end = Window.unboundedFollowing we will get as below:

(
    dfw
    .withColumn(
        "rm",
        F.max("price").over(
            Window
            .partitionBy("name")
            .orderBy("id")
            .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
        )
    )
    .show()
)

#output
+----+---+-----+---+
|name| id|price| rm|
+----+---+-----+---+
| abc|  1|  100|300|
| abc|  2|  200|300|
| abc|  3|  300|300|
| abc|  4|  200|300|
| abc|  5|  100|300|
+----+---+-----+---+
Now as you can see in the same window it's looking downwards in all values for a max instead of limiting it to the current row.

Now third will be start = Window.currentRow and end = Window.unboundedFollowing

(
    dfw
    .withColumn(
        "rm",
        F.max("price").over(
            Window
            .partitionBy("name")
            .orderBy("id")
            .rowsBetween(Window.currentRow, Window.unboundedFollowing)
        )
    )
    .show()
)

#output
+----+---+-----+---+
|name| id|price| rm|
+----+---+-----+---+
| abc|  1|  100|300|
| abc|  2|  200|300|
| abc|  3|  300|300|
| abc|  4|  200|200|
| abc|  5|  100|100|
+----+---+-----+---+
Now it's looking down only for a max starting its row from the current one.

Also, it's not limited to just these 3 to use as is you can even start = Window.currentRow-1 and end = Window.currentRow+1 so instead of looking for all values above or below it will only look at 1 row above and 1 row below.

like this:

(
    dfw
    .withColumn(
        "rm",
        F.max("price").over(
            Window
            .partitionBy("name")
            .orderBy("id")
            .rowsBetween(Window.currentRow-1, Window.currentRow+1)
        )
    )
    .show()
)

# output
+----+---+-----+---+
|name| id|price| rm|
+----+---+-----+---+
| abc|  1|  100|200|
| abc|  2|  200|300|
| abc|  3|  300|300|
| abc|  4|  200|300|
| abc|  5|  100|200|
+----+---+-----+---+
So you can imagine it a window inside the window which works around the current row it's processing.
"""