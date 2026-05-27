from pyspark import pipelines as dp 
from pyspark.sql.functions import col 
 

@dp.materialized_view( 
    name="dbacademy.sdp_gold.customer_status_gold_vw", 
    comment="Gold view joining customers and status data through orders" 

) 

def customer_status_gold_vw(): 

    customers = spark.read.table("dbacademy.sdp_bronze.customers_bronze_raw") 

    orders = spark.read.table("dbacademy.sdp_bronze.orders_bronze") 

    status = spark.read.table("dbacademy.sdp_bronze.status_bronze") 

 

    return ( 

        customers 

        .join(orders, customers.customer_id == orders.customer_id, "inner") 

        .join(status, orders.order_id == status.order_id, "inner") 

        .select( 

            customers.customer_id, 

            customers.city, 

            status.order_id, 

            status.order_status.alias("status"), 

            status.status_timestamp.alias("timestamp") 

        ) 

    ) 

 