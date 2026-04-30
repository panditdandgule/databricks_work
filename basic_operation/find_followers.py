"""
Find Followers Count 
Write a solution that will, for each user, return the number of followers. 
Return the result table ordered by user_id in ascending order.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark =SparkSession.builder.appName("FollowersCount").getOrCreate()

#️⃣ creating list of tuples for followers data
followers_data = [(0, 1),(1, 0),(2, 0),(2, 1)]

#️⃣ specifying columns
followers_cols = ["user_id", "follower_id"]

followers_df = spark.createDataFrame(followers_data,followers_cols)

final_df = followers_df.groupBy("user_id").agg(F.count("follower_id").alias("Followers_count"))

final_df = final_df.orderBy("user_id")

final_df.show()