from pyspark import pipelines as dp 

from pyspark.sql.functions import expr 

 

 

# Create target streaming table for CDC 

dp.create_streaming_table( 

    name="dbacademy.sdp_silver.customer_silver", 

    comment="Silver customer table with SCD Type 2 history tracking" 

) 

 

# Apply CDC changes from the cleaned bronze table 

dp.create_auto_cdc_flow( 

    target="dbacademy.sdp_silver.customer_silver", 

    source="dbacademy.sdp_silver.customer_bronze_clean", 

    keys=["customer_id"], 

    sequence_by="timestamp", 

    apply_as_deletes=expr("operation = 'DELETE'"), 

    except_column_list=["operation", "_rescued_data"], 

    stored_as_scd_type=2 

) 

 