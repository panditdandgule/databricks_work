from pyspark import pipelines as dp 

 

 

@dp.table( 

    name="dbacademy.sdp_bronze.status_bronze", 

    comment="Raw status data ingested from JSON files via Auto Loader" 

) 

def status_bronze(): 

    return ( 

        spark.readStream.format("cloudFiles") 

        .option("cloudFiles.format", "json") 

        .option("cloudFiles.inferColumnTypes", "true") 

        .load("/Volumes/dbacademy/healthcare/status/") 

    ) 

 