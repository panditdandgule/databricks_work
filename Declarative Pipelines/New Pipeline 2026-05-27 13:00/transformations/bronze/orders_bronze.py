from pyspark import pipelines as dp 

 
@dp.table( 

    name="orders_bronze", 

    comment="Raw orders data ingested from JSON files via Auto Loader" 

) 

def orders_bronze(): 

    return ( 

        spark.readStream.format("cloudFiles") 

        .option("cloudFiles.format", "json") 

        .option("cloudFiles.inferColumnTypes", "true") 

        .load("/Volumes/dbacademy/healthcare/orders/") 

    ) 

 