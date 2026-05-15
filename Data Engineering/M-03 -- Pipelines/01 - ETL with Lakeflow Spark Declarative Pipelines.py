# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC Let’s explore the process of ETL with Databricks, focusing on Lakeflow Spark Declarative Pipelines for incremental or streaming processing pipelines.
# MAGIC
# MAGIC So what exactly are Lakeflow Spark Declarative Pipelines? 
# MAGIC
# MAGIC ###Lakeflow Spark Declarative Pipelines Overview
# MAGIC Lakeflow Spark Declarative Pipelines are a declarative ETL framework for the Databricks Data Intelligence Platform that helps data teams simplify streaming and batch ETL cost-effectively. It revolutionizes ETL and real-time analytics by automating and scaling streaming ingestion and transformation, providing powerful pipeline observability. 
# MAGIC
# MAGIC ![get-started-de-lsdp2.png](../Includes/images/get-started-de-lsdp2.png "get-started-de-lsdp2.png")
# MAGIC
# MAGIC With Lakeflow Spark Declarative Pipelines, we're making it dramatically easier to build and manage reliable data pipelines at scale. Let me walk you through how.
# MAGIC
# MAGIC - Simplified Pipeline Authoring
# MAGIC You can now define data ingestion and transformation tasks using familiar SQL or Python. No need to write complex orchestration logic. Lakeflow takes care of the execution plan, error handling, and dependency management behind the scenes.
# MAGIC
# MAGIC - Intelligent Optimization at Scale
# MAGIC As your data volumes grow, Spark Declarative Pipelines automatically scale and recover from failures. This means fewer manual interventions, better reliability, and lower operational overhead.
# MAGIC
# MAGIC - Unified Batch and Streaming
# MAGIC Whether you're processing large historical datasets or working with real-time data, Spark Pipelines handle both seamlessly. They adapt to the workload type and optimize for performance and cost efficiency, no need to manage separate systems or rewrite code.
# MAGIC
# MAGIC Overall, this is about empowering your team to move faster with fewer headaches while delivering production-grade data pipelines that just work.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Connecting to Data Sources
# MAGIC
# MAGIC It all starts with getting your data into Databricks, and that’s where Lakeflow Connect plays a crucial role.
# MAGIC
# MAGIC ![get-started-de-lsdp3.png](../Includes/images/get-started-de-lsdp3.png "get-started-de-lsdp3.png")
# MAGIC
# MAGIC You can bring in data from a variety of sources. Whether it is stored in cloud object stores such as S3, ADLS, or GCS, streaming from message queues like Kafka, Pub/Sub, or Kinesis, pulled from traditional databases including SQL Server or Postgres, or coming from SaaS applications like Salesforce or Workday, Lakeflow Connect makes ingestion simple and reliable.
# MAGIC
# MAGIC <CLICK> Once the data is connected, Lakeflow Declarative Pipelines can handle ingestion and transformation efficiently. This allows you to build data pipelines that follow the medallion architecture, progressing data through bronze, silver, and gold layers with confidence in reliability and scalability.
# MAGIC
# MAGIC No matter what your data source, you can ingest, transform, and operationalize your data quickly, all within the Databricks environment.
# MAGIC
# MAGIC At the end of the day, Spark Declarative Pipelines is for incremental ETL, regardless of whether you are doing batch or streaming processing. Regardless of the data source, which is the domain of Lakeflow Connect, SDP(Spark Declarative Pipelines) is for transitioning your data through the medallion architecture stages.
# MAGIC
# MAGIC Lakeflow Spark Declarative Pipelines uses a simple declarative approach to building reliable data pipelines. With automatic infrastructure management, you can spend time getting value from your data faster without having to spend the time on the tooling. 
