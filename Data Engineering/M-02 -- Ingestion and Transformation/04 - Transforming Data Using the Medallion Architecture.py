# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC # Transforming Data Using the Medallion Architecture
# MAGIC ![get-started-de-medallion.png](../Includes/images/get-started-de-medallion.png "get-started-de-medallion.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Important: Select Environment 4
# MAGIC The cells below may not work in other environments. To choose environment 4: 
# MAGIC 1. Click the ![environment.png](../Includes/images/environment.png "environment.png") button on the right sidebar
# MAGIC 1. Open the **Environment version** dropdown
# MAGIC 1. Select **4**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Classroom Setup
# MAGIC
# MAGIC Run the following cell to configure your working environment for this lesson.

# COMMAND ----------

####################################################################################
# Set python variables for catalog, schema, and volume names (change, if desired)
catalog_name = "dbacademy"
schema_name = "transforming_data"
volume_name = "myfiles"
####################################################################################

####################################################################################
# Create the catalog, schema, and volume if they don't exist already
spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{schema_name}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {catalog_name}.{schema_name}.{volume_name}")
####################################################################################

####################################################################################
# Creates a file called employees.csv in the specified catalog.schema.volume
import pandas as pd
data = [
    ["1111", "Kristi", "USA", "Manager"],
    ["2222", "Sophia", "Greece", "Developer"],
    ["3333", "Peter", "USA", "Developer"],
    ["4444", "Zebi", "Pakistan", "Administrator"]
]
columns = ["ID", "Firstname", "Country", "Role"] 
df = pd.DataFrame(data, columns=columns)
file_path = f"/Volumes/{catalog_name}/{schema_name}/{volume_name}/employees.csv"
df.to_csv(file_path, index=False)
################################################################################

####################################################################################
# Creates a file called employees2.csv in the specified catalog.schema.volume
data = [
    [5555, 'Alex','USA', 'Instructor'],
    [6666, 'Sanjay','India', 'Instructor']
]
columns = ["ID","Firstname", "Country", "Role"]

## Create the DataFrame
df = pd.DataFrame(data, columns=columns)

## Create the CSV file in the course Catalog.Schema.Volume
df.to_csv(f"/Volumes/{catalog_name}/{schema_name}/{volume_name}/employees2.csv", index=False)
####################################################################################

# COMMAND ----------

# MAGIC %md
# MAGIC ## A. Configure and Explore Your Environment

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Set the default catalog and schema.

# COMMAND ----------

## Set the default catalog and schema
spark.sql(f"USE CATALOG {catalog_name}")
spark.sql(f"USE SCHEMA {schema_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC 2. View the available files in your schema's **myfiles** volume. Confirm that the volume contains two CSV files, **employees.csv** and **employees2.csv**.

# COMMAND ----------

spark.sql(f"LIST '/Volumes/{catalog_name}/{schema_name}/{volume_name}/' ").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## B. Simple Example of the Medallion Architecture

# COMMAND ----------

# MAGIC %md
# MAGIC ### BRONZE
# MAGIC **Objective:** Create a table using all of the CSV files in the **myfiles** volume.

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Execute the cell to perform the following steps:
# MAGIC
# MAGIC     - The `DROP TABLE IF EXISTS` statement drops the **current_employees_bronze** table if it already exists (for demonstration purposes).
# MAGIC     
# MAGIC     - The `CREATE TABLE IF NOT EXISTS` statement creates the Delta table **current_employees_bronze** if it doesn't already exist and defines its columns.
# MAGIC     
# MAGIC     - The `COPY INTO` statement:
# MAGIC         - Loads all the CSV files from the **myfiles** volume in the schema into the **current_employees_bronze** table.
# MAGIC         - Uses the first row as headers and infers the schema from the CSV files.
# MAGIC     
# MAGIC     - The final `SELECT` query displays all rows from the **current_employees_bronze** table.
# MAGIC
# MAGIC
# MAGIC View the results and confirm that the table contains **6 rows** and **4 columns**.
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Drop the table if it exists for demonstration purposes
# MAGIC DROP TABLE IF EXISTS current_employees_bronze;
# MAGIC
# MAGIC -- Create an empty table and columns
# MAGIC CREATE TABLE IF NOT EXISTS current_employees_bronze (
# MAGIC   ID INT,
# MAGIC   FirstName STRING,
# MAGIC   Country STRING,
# MAGIC   Role STRING
# MAGIC   );

# COMMAND ----------

## Create the bronze raw ingestion table and include the CSV file name for the rows
spark.sql(f'''
  COPY INTO current_employees_bronze
  FROM '/Volumes/{catalog_name}/{schema_name}/{volume_name}/'
  FILEFORMAT = CSV
  FORMAT_OPTIONS (
    'header' = 'true', 
    'inferSchema' = 'true'
)
''').display()

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM current_employees_bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC ### SILVER
# MAGIC **Objective**: Transform the bronze table and create the silver table.
# MAGIC
# MAGIC 1. Create a table named **current_employees_silver** from the **current_employees_bronze** table. 
# MAGIC
# MAGIC     The table will:
# MAGIC     - Select the columns **ID**, **FirstName**, **Country**.
# MAGIC     - Convert the **Role** column to uppercase.
# MAGIC     - Add two new columns: **CurrentTimeStamp** and **CurrentDate**.

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create a temporary view to use to merge the data into the final silver table
# MAGIC CREATE OR REPLACE TABLE current_employees_silver AS 
# MAGIC SELECT 
# MAGIC   ID,
# MAGIC   FirstName,
# MAGIC   Country,
# MAGIC   upper(Role) as Role,                 -- Upcase the Role column
# MAGIC   current_timestamp() as CurrentTimeStamp,    -- Get the current datetime
# MAGIC   date(CurrentTimeStamp) as CurrentDate       -- Get the date
# MAGIC FROM current_employees_bronze;

# COMMAND ----------

# MAGIC %md
# MAGIC 2. View the **current_employees_silver** table. Confirm that the table contains 6 rows and 6 columns.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM current_employees_silver;

# COMMAND ----------

# MAGIC %md
# MAGIC ### GOLD
# MAGIC **Objective:** Aggregate the silver table to create the final gold table.

# COMMAND ----------

# MAGIC %md
# MAGIC 1. Create a temporary view named **temp_view_total_roles** that aggregates the total number of employees by role. Then, display the results of the view.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW temp_view_total_roles AS 
# MAGIC SELECT
# MAGIC   Role, 
# MAGIC   count(*) as TotalEmployees
# MAGIC FROM current_employees_silver
# MAGIC GROUP BY Role;
# MAGIC
# MAGIC
# MAGIC SELECT *
# MAGIC FROM temp_view_total_roles;

# COMMAND ----------

# MAGIC %md
# MAGIC 2. Create the final gold table named **total_roles_gold** with the specified columns.

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS total_roles_gold (
# MAGIC   Role STRING,
# MAGIC   TotalEmployees INT
# MAGIC );

# COMMAND ----------

# MAGIC %md
# MAGIC 3. Insert all rows from the aggregated temporary view **temp_view_total_rows** into the **total_roles_gold** table, overwriting the existing data in the table. This overwrites the data in a table but keeps the existing schema and table definition and properties.
# MAGIC
# MAGIC     Confirm the following:
# MAGIC     - **num_affected_rows** is *4*
# MAGIC     - **num_inserted_rows** is *4*

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT OVERWRITE TABLE total_roles_gold
# MAGIC SELECT * 
# MAGIC FROM temp_view_total_roles;

# COMMAND ----------

# MAGIC %md
# MAGIC 4. Query the **total_roles_gold** table to view the total number of employees by role.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM total_roles_gold;

# COMMAND ----------

# MAGIC %md
# MAGIC 5. View the history of the **total_roles_gold** table.

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY total_roles_gold;

# COMMAND ----------

# MAGIC %md
# MAGIC ## C. Data Governance and Security
# MAGIC **Objectives:** View the lineage of the **total_roles_gold** table and learn how to set its permissions.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Complete the following to open the schema in the **Catalog Explorer**.
# MAGIC
# MAGIC a. Select the Catalog icon ![catalog_icon](../Includes/images/catalog_icon.png) in the left navigation bar. 
# MAGIC
# MAGIC c. Select the refresh icon ![refresh_icon](../Includes/images/refresh_icon.png) to refresh the catalog.
# MAGIC
# MAGIC d. Expand the catalog (default is **dbacademy**). Within the catalog, you should see a few schemas (databases).
# MAGIC
# MAGIC e. Find and select the **transforming_data** schema.
# MAGIC
# MAGIC f.  Click the options icon ![options_icon](../Includes/images/options_icon.png) to the right of the schema name and choose **Open in Catalog Explorer**.
# MAGIC
# MAGIC g. Notice that the three tables we created in the demo: **current_employees_bronze**, **current_employees_silver**, and **total_roles_gold** are shown in the **Catalog Explorer** for your schema.
# MAGIC
# MAGIC h. In the **Catalog Explorer** select the **total_roles_gold** table.
# MAGIC
# MAGIC Leave the **Catalog Explorer** tab open.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Complete the following to view the **total_roles_gold** table's permissions, history, lineage and insights in Catalog Explorer: 
# MAGIC
# MAGIC    a. **Permissions**. 
# MAGIC
# MAGIC   - Select the **Permissions** tab. This will display all permissions on the table. Currently the table does not have any permissions set.
# MAGIC
# MAGIC   - Select **Grant**. This allows you to add multiple principals and assign privileges to them. Users must have access to the Catalog and Schema of the table.
# MAGIC   
# MAGIC   - Select **Cancel**. 
# MAGIC
# MAGIC    b. **History**
# MAGIC
# MAGIC   - Select the **History** tab. If needed, click **Select compute** and choose the default compute from the dropdown. This will display the table's history. The **total_roles_gold** table currently has two versions. 
# MAGIC
# MAGIC    c. **Lineage**
# MAGIC
# MAGIC   - Select the **Lineage** tab. This displays the table's lineage. Confirm that the **current_employees_silver** table is shown.
# MAGIC
# MAGIC   - Select the **See lineage graph** button ![see_lineage_graph_button](../Includes/images/see_lineage_graph_button.png). This displays the table's lineage visually. You can select the ![plus_button](../Includes/images/plus_button.png) icon to zoom in.
# MAGIC
# MAGIC   - Close out of the lineage graph.
# MAGIC
# MAGIC    d. **Insights**
# MAGIC
# MAGIC   - Select the **Insights** tab. You can use the Insights tab in **Catalog Explorer** to view the most frequent recent queries and users of any table registered in Unity Catalog. The Insights tab reports on frequent queries and user access for the past 30 days.
# MAGIC   
# MAGIC    e. Close the **Catalog Explorer** browser tab. 

# COMMAND ----------

# MAGIC %md
# MAGIC ##D. Cleanup
# MAGIC 1. Drop the **transforming_data** schema.

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP SCHEMA IF EXISTS transforming_data CASCADE;
