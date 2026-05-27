from pyspark import pipelines as dp 

from pyspark.sql.functions import col 

 

 

@dp.materialized_view( 

    name="dbacademy.sdp_gold.customer_orders_gold_vw", 

    comment="Gold view joining customers and orders data" 

) 

def customer_orders_gold_vw(): 

    customers = spark.read.table("dbacademy.sdp_bronze.customers_bronze_raw") 

    orders = spark.read.table("dbacademy.sdp_bronze.orders_bronze") 

 

    return ( 

        customers.join(orders, customers.customer_id == orders.customer_id, "inner") 

        .select( 

            customers.customer_id, 

            customers.city, 

            orders.order_id, 

            orders.notifications.alias("notification"), 

            orders.order_timestamp.alias("timestamp") 

        ) 

    ) 