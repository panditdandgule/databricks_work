from pyspark.sql import functions as F
from pyspark import pipelines as dp

SOURCE_PATH = '/Volumes/cabs/bronze/raw_data/trips/full_load/'

@dp.table(
    name = "cabs.bronze.trips",
    comment = "Streaming ingestion of raw orders data with Autoloader",
    table_properties={
        "quality":"bronze",
        "layer":"bronze",
        "delta.enableChangeDataFeed":"true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true"
    }
)

def orders_bronze():
    df = (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format","csv")
        .option("cloudFiles.inferColumnTypes","true")
        .option("cloudFiles.schemaEvolutionMode","rescue")
        .option("cloudFiles.maxFilesPerTrigger",100)
        .load(SOURCE_PATH)
    )

     # Rename the problematic column
    df = df.withColumnRenamed(
        "distance_travelled(km)",
        "distance_travelled_km"
    )

    df = df.withColumn("file_name", F.col("_metadata.file_path")).withColumn("ingest_datetime", F.current_timestamp())

    return df