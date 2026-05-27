from pyspark import pipelines as dp 

 

 

@dp.table( 

    name="dbacademy.sdp_silver.orders_silver", 

    comment="Silver orders table with data quality constraints applied" 

) 

@dp.expect( 

    "valid_notifications", 

    "notifications IN ('Y', 'U')" 

) 

@dp.expect_or_drop( 

    "valid_order_timestamp", 

    "order_timestamp > 1640390400" 

) 

@dp.expect_or_fail( 

    "valid_customer_id", 

    "customer_id IS NOT NULL" 

) 

def orders_silver(): 

    return spark.readStream.table("dbacademy.sdp_bronze.orders_bronze") 

 