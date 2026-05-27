from pyspark import pipelines as dp 

 

 

@dp.table( 

    name="dbacademy.sdp_silver.status_silver", 

    comment="Silver status table with filtered order statuses" 

) 

@dp.expect_or_drop( 

    "valid_status_timestamp", 

    "status_timestamp > 1640390400" 

) 

@dp.expect( 

    "valid_order_status", 

    "order_status IN ('on the way', 'canceled', 'return canceled', 'delivered', 'return processed', 'placed', 'preparing')" 

) 

@dp.expect_or_drop( 

    "filter_valid_order_status", 

    "order_status IN ('on the way', 'canceled', 'return canceled', 'delivered', 'return processed', 'placed', 'preparing')" 

) 

def status_silver(): 

    return spark.readStream.table("dbacademy.sdp_bronze.status_bronze") 

 