# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC # Task 1 - Setup and Bronze Table
# MAGIC This notebook is used for task 1 in the job from the directions in notebook: **02-Creating a Simple Lakeflow Job**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Capture Job Parameters

# COMMAND ----------

catalog_name = dbutils.widgets.get("catalog_name")
schema_name = dbutils.widgets.get("schema_name")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configure Your Environment

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Set the default catalog and schema.

# COMMAND ----------

# Set the catalog and schema
spark.sql(f'USE CATALOG {catalog_name}')
spark.sql(f'USE SCHEMA {schema_name}')

# COMMAND ----------

# MAGIC %md
# MAGIC ### BRONZE
# MAGIC **Objective:** Create a table using all of the CSV files in the **myfiles** volume.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create an empty table and columns
# MAGIC CREATE TABLE IF NOT EXISTS current_employees_bronze_job (
# MAGIC   ID INT,
# MAGIC   FirstName STRING,
# MAGIC   Country STRING,
# MAGIC   Role STRING
# MAGIC   );

# COMMAND ----------

# Create the bronze raw ingestion table and include the file name for the rows
spark.sql(f'''
  COPY INTO current_employees_bronze_job
  FROM '/Volumes/{catalog_name}/{schema_name}/myfiles/'
  FILEFORMAT = CSV
  FORMAT_OPTIONS (
    'header' = 'true', 
    'inferSchema' = 'true'
)
''').display()
