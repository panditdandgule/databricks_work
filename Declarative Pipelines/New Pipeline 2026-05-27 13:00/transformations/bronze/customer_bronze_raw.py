from pyspark import pipelines as dp 

@dp.table( 

    name="customers_bronze_raw", 

    comment="Raw customer data ingested from JSON files via Auto Loader" 

) 

def customers_bronze_raw(): 

    return ( 

        spark.readStream.format("cloudFiles") 

        .option("cloudFiles.format", "json") 

        .option("cloudFiles.inferColumnTypes", "true") 

        .load("/Volumes/dbacademy/healthcare/customers/*.json") 

    ) 

 