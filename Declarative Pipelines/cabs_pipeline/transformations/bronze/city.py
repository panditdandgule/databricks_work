from pyspark import pipelines as dp
from pyspark.sql import functions as F


# Configuration
SOURCE_PATH ="/Volumes/cabs/bronze/raw_data/city/"

@dp.materialized_view(
    name = "cabs.bronze.city",
    comment= "City Raw Data Processing",
    table_properties={
        "quality" : "bronze",
        "layer" : "bronze",
        "source_format" : "csv",
        "delta.enableChangeDataFeed" : "true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true"
    }
)


def city_bronze():

    df = (
        spark.read.format("csv")
        .option("header","true")
        .option("inferSchema","true")
        .option("mergeSchema","true")
        .option("mode","PERMISSIVE")
        .option("columnNameCorruptRecord","_corrupt_record")
        .load(SOURCE_PATH)
    )
    df = df.withColumn("file_name",F.col("_metadata.file_path")).withColumn("ingestion_time",F.current_timestamp())
    
    return df
