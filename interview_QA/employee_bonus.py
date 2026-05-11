"""

➡️ Problem Statement:
Write a solution to report the name and bonus amount of each employee with a bonus less than 1000. 
Return the result table in any order.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType,StructField,IntegerType,StringType

schema =  StructType([StructField("empId",IntegerType(),nullable=True),
                      StructField("name",StringType(),nullable=True),
                      StructField("supervisor",StringType(),nullable=False),
                      StructField("salary",IntegerType(),nullable=False)])

#Createing spark session
spark = SparkSession.builder.appName("EmployeeBonus").getOrCreate()

# creating employees dataframe
employee_data = [(3,"Brad","null",4000), (1,"John",3,1000), (2,"Dan",3,2000), (4,"Thomas",3,4000)]
employee_cols = ("empId","name","supervisor","salary")

emp_df = spark.createDataFrame(employee_data,schema)

# creating bonus dataframe
bonus_data = [(2,500),(4,2000)]
bonus_cols = ("empId","bonus")
bonus_df = spark.createDataFrame(bonus_data, bonus_cols)
bonus_df = bonus_df.withColumn("empId",F.col("empId").cast("int"))

joined_df = emp_df.join(bonus_df,on="empId",how='left')

joined_df = joined_df.filter((F.col("bonus")<1000) | (F.col("bonus").isNull()))

joined_df = joined_df.select("name","bonus")
