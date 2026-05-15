# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Transformation Overview
# MAGIC Within the Lakehouse, you will process data using Apache Spark, an open-source, in-memory distributed processing engine. It’s scalable and supports batch and streaming operations, as well as SQL, Python, Scala, and more.
# MAGIC
# MAGIC With Databricks you can also enable Photon. Photon is a high-performance query engine for Databricks that can optimize SQL queries and accelerate processing with Delta Lake.
# MAGIC
# MAGIC When processing data, Databricks recommends using the Medallion Architecture (sometimes known as Multi Hop architecture) for transforming data in our data processing component within the Data Engineering architecture. Let’s review the medallion architecture at a high level.
# MAGIC
# MAGIC Let’s break down how this architecture works in practice.
# MAGIC
# MAGIC ![get-started-de-medallion.png](../Includes/images/get-started-de-medallion.png "get-started-de-medallion.png")
# MAGIC
# MAGIC As you ingest data into your Delta Lake through batch or streaming methods, or both, you can begin processing and transforming your data in Databricks. 
# MAGIC
# MAGIC For almost all Delta Lake use cases, we frame our data transformation pipelines as the medallion architecture, a data design pattern used to organize data within a lakehouse. This is built on the “bronze-silver-gold medallion” data quality levels.  Of course, Databricks did not invent this pattern, but it is a very good fit for Delta Lake. 
# MAGIC
# MAGIC The goal is to incrementally and progressively improve the structure and quality of data as it moves through each layer: From the original raw data in your data lake in its native format, to the Bronze layer to the Silver layer and finally to the Gold layer consumer level data.
# MAGIC
# MAGIC Now, let’s explore the three layers of the Medallion Architecture.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Bronze
# MAGIC In the bronze layer, we simply ingest raw data from external source systems.  We get the data in as quickly as possible, even though it may be dirty.  We keep the data, making it useful for both current and future projects. Adding any additional metadata columns that capture the load date/time, process ID, and more.
# MAGIC
# MAGIC By ingesting the data “raw,” we avoid exposing ourselves to bugs in the system or the processing logic.  We have the data as it originally existed, and we can always “go back” to it.  This is feasible because storage is so cheap.
# MAGIC
# MAGIC Depending on your regulatory requirements, you can also remove any personally identifiable information (PII) as you ingest data into your Delta Lake.
# MAGIC
# MAGIC Once raw data is in Bronze, we refine it further in the Silver layer.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Silver
# MAGIC In the silver layer of the Lakehouse, data is filtered, cleansed, joined, and enriched version of the bronze data. The tables in the silver layer define the structure of the data, and enforce the schema, or evolve the schema as necessary.
# MAGIC
# MAGIC The silver layer becomes a “single source of truth” for the enterprise across many projects.  We fix errors, add in business data, apply business rules, etc. Examples of data in this layer would be cleaned tables like all unique customers, transactions, and more.
# MAGIC
# MAGIC After cleansing in Silver, data is optimized for consumption in Gold.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Gold
# MAGIC Gold-level tables contain clean data, ready for consumer consumption. 
# MAGIC
# MAGIC Depending on the use case, they may include business-level aggregates of the Silver data. 
# MAGIC
# MAGIC Gold data is formatted for specific projects or reports delivered downstream to users and applications. These tables can be stored in Delta format for use by Spark jobs or SQL queries and may also be replicated to external systems. Many engines have Delta Lake readers, and with Uniform, Delta tables can also be read natively by other applications.
# MAGIC
# MAGIC With Gold data ready, let’s see how Delta Lake’s features support this workflow.
# MAGIC
# MAGIC Thanks to the solid foundation of Delta’s ACID support, Databricks can offer more advanced features in the runtime itself. For example, Databricks is able to provide support for deletes, updates, and merges. These features are groundbreaking for data lakes. Moreover, Delta Lake is extremely easy to use. It supports full SQL, the simplest, most powerful, and most well-known API for data, as well as Python and Scala. 
# MAGIC
# MAGIC With ACID compliance and SQL support, it becomes much easier to manage your data pipelines in the face of change. For example, when business logic changes, you can simply update or delete your Silver and Gold tables, and restart your stream or batch processes in order to put the changes into effect. 
# MAGIC
# MAGIC While this architecture is robust, real-world pipelines often add complexity.
# MAGIC
# MAGIC ![get-started-de-medallion2.png](../Includes/images/get-started-de-medallion2.png "get-started-de-medallion2.png")
# MAGIC
# MAGIC Typically, a data engineering pipeline is quite complex. It involves several stages, starting with reading data from various sources, including streaming data, batch files, and data lakes.
# MAGIC - Data from these external sources is ingested into bronze tables in its raw form.
# MAGIC - The bronze data is then processed to create multiple silver layer tables, which are cleaned and joined to enhance data quality.
# MAGIC - Finally, the cleaned and processed silver tables are aggregated into gold tables. These gold tables are used for various purposes, including BI and reporting, machine learning, AI, and streaming tasks to support business needs.
# MAGIC
# MAGIC Understanding these layers equips you to design scalable, reliable data pipelines.
