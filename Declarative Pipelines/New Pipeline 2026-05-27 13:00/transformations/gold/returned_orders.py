from pyspark import pipelines as dp 
from pyspark.sql.functions import col 

@dp.materialized_view( 
    name="dbacademy.sdp_gold.returned_orders", 
    comment="Gold view showing only returned order statuses (return canceled and return processed)" 

) 

def returned_orders(): 

    return ( 

        spark.read.table("dbacademy.sdp_gold.order_status") 

        .filter(col("order_status").isin("return canceled", "return processed")) 

    ) 

 

 