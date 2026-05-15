from pyspark import pipelines as dp
from pyspark.sql import functions as F

SOURCE_PATH ='s3://pnd-acm-340b/autoloader_source/'

@dp.materialized_view(
    name="dlt_catalog.raw.raw_customers",
    comment="customers Raw Data Processing",
    table_properties={
        "quality": "bronze",
        "layer": "bronze",
        "source_format": "parquet",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true"
    }
)
def bronze_customers():
    df = df = spark.read.format("parquet").load(SOURCE_PATH)
    return df

@dp.materialized_view(
    name="dlt_catalog.raw.silver_customers",
    comment="customers Staging Data Processing",
    table_properties={
        "quality": "silver",
        "layer": "silver",
        "source_format": "parquet",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true"
    }
)
def silver_customers():
    df = spark.read.table("dlt_catalog.raw.raw_customers")
    df = df.withColumn("customer_id", F.col("id"))
    df = df.drop("id")
    return df

@dp.materialized_view(
    name="dlt_catalog.raw.gold_customers",
    comment="customers Staging Data Processing",
    table_properties={
        "quality": "gold",
        "layer": "gold",
        "source_format": "parquet",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true"
    }
)
def gold_customers():
    df = spark.read.table("dlt_catalog.raw.silver_customers")
    return df