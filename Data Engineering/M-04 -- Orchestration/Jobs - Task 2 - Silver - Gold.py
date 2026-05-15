# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC # Task 2 - Silver - Gold Table
# MAGIC This notebook is used for task 2 in the job from the directions in notebook: **Jobs - Creating a Simple Lakeflow Job**

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
# MAGIC ### SILVER
# MAGIC **Objective**: Transform the bronze table and create the silver table.
# MAGIC
# MAGIC 1. Create a table named **current_employees_silver_job** from the **current_employees_bronze_job** table. 
# MAGIC
# MAGIC     The table will:
# MAGIC     - Select the columns **ID**, **FirstName**, **Country**.
# MAGIC     - Convert the **Role** column to uppercase.
# MAGIC     - Add two new columns: **CurrentTimeStamp** and **CurrentDate**.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create a temporary view to use to merge the data into the final silver table
# MAGIC CREATE OR REPLACE TABLE current_employees_silver_job AS 
# MAGIC SELECT 
# MAGIC   ID,
# MAGIC   FirstName,
# MAGIC   Country,
# MAGIC   upper(Role) as Role,                 -- Upcase the Role column
# MAGIC   current_timestamp() as CurrentTimeStamp,    -- Get the current datetime
# MAGIC   date(CurrentTimeStamp) as CurrentDate       -- Get the date
# MAGIC FROM current_employees_bronze_job;

# COMMAND ----------

# MAGIC %md
# MAGIC ### GOLD
# MAGIC **Objective:** Aggregate the silver table to create the final gold table.

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Create a temporary view named **temp_view_total_roles_job** that aggregates the total number of employees by role. Then, display the results of the view.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW temp_view_total_roles_job AS 
# MAGIC SELECT
# MAGIC   Role, 
# MAGIC   count(*) as TotalEmployees
# MAGIC FROM current_employees_silver_job
# MAGIC GROUP BY Role;

# COMMAND ----------

# MAGIC %md
# MAGIC 2. Create the final gold table named **total_roles_gold_job** with the specified columns.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS total_roles_gold_job (
# MAGIC   Role STRING,
# MAGIC   TotalEmployees INT
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC 3. Insert all rows from the aggregated temporary view **temp_view_total_roles_job** into the **total_roles_gold_job** table, overwriting the existing data in the table. This overwrites the data in a table but keeps the existing schema and table definition and properties.
# MAGIC
# MAGIC     Confirm the following:
# MAGIC     - **num_affected_rows** is *4*
# MAGIC     - **num_inserted_rows** is *4*

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE TABLE total_roles_gold_job
# MAGIC SELECT * 
# MAGIC FROM temp_view_total_roles_job;
