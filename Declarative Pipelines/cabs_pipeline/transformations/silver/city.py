from pyspark.sql import functions as F
from pyspark import pipelines as dp

@dp.materialized_view(
    name = "cabs.silver.city",
    comment = "Silver table for city",
    table_properties = {
        "quality" : "silver",
        "layer" : "silver",
        "delta.enableChangeDataFeed":"true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true"
    }
)

def city_silver():
    df_bronze = spark.read.table("cabs.bronze.city")

    df = (df_bronze.select(F.col("city_id").alias("city_id"),
                           F.col("city_name").alias("city_name"),
                           F.col("ingestion_time").alias("bronze_ingest_date_time")
                           )
          )

    df_silver = df.withColumn("silver_processed_timestamp",F.current_timestamp())

    return df_silver