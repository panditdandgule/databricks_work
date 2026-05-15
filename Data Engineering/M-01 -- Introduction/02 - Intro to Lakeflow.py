# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lakeflow Overview
# MAGIC
# MAGIC Achieving data intelligence starts with getting data into the platform which is the domain of data engineering. Data Engineering involves not only getting data into the platform but also transforming that data into useable assets and managing this at scale. Databricks provides a powerful solution for this with Databricks Lakeflow. 
# MAGIC
# MAGIC Let’s take a closer look at the core features of Lakeflow.
# MAGIC
# MAGIC ![get-started-de-lakeflow-features.png](../Includes/images/get-started-de-lakeflow-features.png "get-started-de-lakeflow-features.png")
# MAGIC
# MAGIC Lakeflow consists of three powerful components:
# MAGIC - Connect for fast, no-code data ingestion from any source;
# MAGIC - Spark Declarative Pipelines for automated and reliable batch or streaming transformations using SQL;
# MAGIC - Jobs for smart orchestration with real-time triggers and monitoring.
# MAGIC
# MAGIC Together, they deliver a seamless, fully governed data engineering workflow within Databricks.
# MAGIC
# MAGIC Let's look at a high level overview of each component of Lakeflow.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Lakeflow Connect
# MAGIC
# MAGIC So what exactly is Lakeflow Connect?
# MAGIC
# MAGIC ![get-started-de-managed-connectors.png](../Includes/images/get-started-de-managed-connectors.png "get-started-de-managed-connectors.png")
# MAGIC
# MAGIC Lakeflow Connect provides simple, efficient connectors to ingest data into the Databricks Lakehouse from a wide range of sources, including enterprise applications, databases, cloud storage, local files, message buses, and more. It supports three main types of ingestion:
# MAGIC - Manual File Uploads: This allows users to upload local files directly to Databricks into either a volume or as a table, making it extremely easy to bring local data into the platform quickly.
# MAGIC - Standard Connectors: These connectors support data ingestion from various sources such as cloud object storage, Kafka, and more. They support multiple ingestion modes, including batch, incremental batch, and streaming. We’ll explore these ingestion methods in more detail shortly.
# MAGIC - Managed Connectors: Purpose-built for ingesting data from enterprise applications, including SaaS platforms and databases. They leverage efficient incremental read/write patterns to provide scalable, cost-effective, and high-performance data ingestion into the lakehouse.
# MAGIC
# MAGIC Taking a closer look at Lakeflow Connect Managed Connectors, they offer built-in, no-code connectors for popular databases and enterprise applications. With a simple interface, it enables fast, scalable, and secure data ingestion into the Databricks platform, all governed by Unity Catalog and powered by serverless compute. With Unity Catalog, data is kept automatically updated, and ensures full observability, governance, and autoscaling across the data ecosystem.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Lakeflow Spark Declarative Pipelines
# MAGIC
# MAGIC Once data is ingested, Lakeflow Spark Declarative Pipelines accelerates ETL with declarative SQL, allowing analysts to build production-grade incremental batch and streaming pipelines. Spark Declarative Pipelines support the medallion architecture, incremental processing, and intelligent workload optimization for faster and more efficient ETL pipelines.
# MAGIC
# MAGIC ![get-started-de-lsdp.png](../Includes/images/get-started-de-lsdp.png "get-started-de-lsdp.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Lakeflow Jobs
# MAGIC
# MAGIC Finally, Lakeflow Jobs simplifies orchestration with smart triggers, real-time monitoring, and automated workloads. Its serverless design supports event-based triggers, continuous execution, and complex DAGs, ensuring reliable and scalable production workloads.
# MAGIC
# MAGIC With Lakeflow Connect, Pipelines, and Jobs, you can streamline your entire data workflow, from ingestion to orchestration, all within the Databricks platform.
# MAGIC
# MAGIC ![get-started-de-lakeflow jobs.png](../Includes/images/get-started-de-lakeflow jobs.png "get-started-de-lakeflow jobs.png")
