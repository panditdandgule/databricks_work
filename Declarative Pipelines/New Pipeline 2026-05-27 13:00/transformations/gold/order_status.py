from pyspark import pipelines as dp 

from pyspark.sql.functions import col 

 

 

@dp.materialized_view( 

    name="order_status", 

    comment="Gold view joining orders and status data" 

) 

def order_status(): 

    orders = spark.read.table("dbacademy.sdp_bronze.orders_bronze") 

    status = spark.read.table("dbacademy.sdp_bronze.status_bronze") 

 

    return ( 

        orders.join(status, orders.order_id == status.order_id, "inner") 

        .select( 

            orders.order_id, 

            orders.order_timestamp, 

            status.order_status, 

            status.status_timestamp.alias("order_status_timestamp") 

        ) 

    ) 

 

 