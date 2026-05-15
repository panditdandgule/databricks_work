# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lakeflow Connect Ingestion Techniques Overview
# MAGIC
# MAGIC Let’s focus on Delta Lake Lakeflow Connect techniques—specifically, how to bring raw data into our Delta Lake.
# MAGIC ![get-started-de-ingestion.png](../Includes/images/get-started-de-ingestion.png "get-started-de-ingestion.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Upload UI
# MAGIC Provides a point and click interface to upload files to create a table. With the Upload UI you can ingest CSV, TSV, JSON, Avro, Parquet, or text files. The Upload to volume UI allows you to upload files in any format to a Unity Catalog volume, including structured, semi-structured, and unstructured data. They represent a logical volume of storage in a cloud object storage location. Volumes are intended for path-based data access to files only. Use tables when you want to work with tabular data in Unity Catalog.

# COMMAND ----------

# MAGIC %md
# MAGIC ### `CREATE TABLE AS (CTAS)`
# MAGIC Creates a table by selecting data from an existing table or data source. By default, it creates a Delta table in Databricks. You can explicitly specify the USING DELTA keyword when creating a table, but *this is optional*.
# MAGIC
# MAGIC `CREATE TABLE mydeltatable`
# MAGIC
# MAGIC `USING DELTA` <--- Optional
# MAGIC
# MAGIC `AS`
# MAGIC
# MAGIC `your query` 

# COMMAND ----------

# MAGIC %md
# MAGIC ### `COPY INTO` 
# MAGIC Offers several advantages for Lakeflow Connect into Delta lake.
# MAGIC First it loads one or more files from a file location into a Delta table.
# MAGIC It supports various file formats and cloud storage locations. 
# MAGIC It automatically handles schema changes, seamlessly integrating new data formats without manual adjustments.
# MAGIC Lastly, it’s idempotent, meaning it will skip files that have already been loaded, increasing efficiency.
# MAGIC
# MAGIC `COPY INTO mydeltatable`
# MAGIC
# MAGIC `FROM ‘your-path’`
# MAGIC
# MAGIC `FILE_FORMAT = ‘format’`
# MAGIC
# MAGIC `FILE_OPTIONS = (‘format-options’) `

# COMMAND ----------

# MAGIC %md
# MAGIC ### Auto Loader 
# MAGIC Incrementally and efficiently processes new data files as they arrive in cloud storage based on an input directory path. It receives notifications from the cloud source and ingests only new files, reducing the need for full reprocessing and enhancing efficiency. 
# MAGIC Auto Loader also automatically infers and evolves schemas, detecting new columns and handling schema changes without manual intervention. 
# MAGIC Additionally, it can "rescue" unexpected data, such as data with differing types, and set it aside for review.
