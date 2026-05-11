from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("HealthCareClaims").getOrCreate()

data = [(101,"patient1",20000,"claimA"),
        (102,"patient1",20000,"claimA"),
        (103,"patient2",60000,"claimB"),
        (104,"patient3",30000,"claimC"),
        (105,"patient2",60000,"claimB")]

df = spark.createDataFrame(data,["claim_id","patient_id","amount","claim_code"])

#step 3: Remove duplicate claims
dedup_df = df.dropDuplicates(subset=["patient_id","claim_code","amount"])

high_cost_df = dedup_df.filter(F.col("amount")>50000)

dedup_df.show()

high_cost_df.show()

