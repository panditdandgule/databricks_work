from pyspark import pipelines as dp 

 

@dp.table( 

    name="dbacademy.sdp_silver.customer_bronze_clean", 

    comment="Cleaned customer bronze data with data quality expectations applied" 

) 

@dp.expect_or_drop( 

    "valid_customer_id", 

    "customer_id IS NOT NULL" 

) 

@dp.expect_or_drop( 

    "valid_operation", 

    "operation IN ('INSERT', 'UPDATE', 'DELETE')" 

) 

@dp.expect_or_drop( 

    "valid_name", 

    "((operation IN ('INSERT', 'UPDATE') AND name IS NOT NULL) OR operation = 'DELETE')" 

) 

@dp.expect_or_drop( 

    "valid_address_fields", 

    "((operation = 'INSERT' AND address IS NOT NULL AND city IS NOT NULL AND state IS NOT NULL AND zip_code IS NOT NULL) OR operation IN ('UPDATE', 'DELETE'))" 

) 

@dp.expect_or_drop( 

    "valid_email", 

    "((operation IN ('INSERT', 'UPDATE') AND email RLIKE '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\\\.[a-zA-Z]{2,}$') OR operation = 'DELETE')" 

) 

def customer_bronze_clean(): 

    return spark.readStream.table("customers_bronze_raw") 

 