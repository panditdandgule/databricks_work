# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC # Monitoring and Optimizing Pipelines
# MAGIC
# MAGIC You can monitor Lakeflow Spark Declarative Pipelines as they run and after a run to optimize, debug, and enrich your ETL logic.
# MAGIC
# MAGIC **Objective:** Use Databricks Lakeflow Spark Declarative Pipelines to monitor an ETL pipeline using the event log, and add data quality expectations.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Important: Select Environment 4
# MAGIC The cells below may not work in other environments. To choose environment 4: 
# MAGIC 1. Click the ![environment.png](../Includes/images/environment.png "environment.png") button on the right sidebar
# MAGIC 1. Open the **Environment version** dropdown
# MAGIC 1. Select **4**

# COMMAND ----------

# MAGIC %md
# MAGIC ## Source Code and Data Quality Expectations
# MAGIC The Lakeflow Pipelines UI provides an IDE experience for developing pipelines. We can view any source code file added to the pipeline and edit it in place. To do this:
# MAGIC
# MAGIC 1. Click the name of the only source code file, **Pipeline - 1.py**, in the workspace pane on the left side of the page.
# MAGIC
# MAGIC This opens the file in the center pane of the page.
# MAGIC
# MAGIC 2. Read through the comments on the source code page to get more information about pipeline syntax, data quality expectations, etc.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Run the Pipeline
# MAGIC
# MAGIC Run the pipeline by clicking **Run pipeline** in the upper-right corner of the pipeline UI

# COMMAND ----------

# MAGIC %md
# MAGIC ## Monitor a Pipeline While Running
# MAGIC As soon as you have started the pipeline: 
# MAGIC 1. In the left workspace pane, at the top of the pane, a counter has begun counting up the number of seconds that the pipeline run has taken. Click the time. This opens the pipeline's "Runs" page.
# MAGIC 2. If it is not already enabled, turn on **New pipeline monitoring** by clicking the clicking the dropdown at the top-left of the page and switching the feature on.
# MAGIC
# MAGIC This page allows you to monitor the pipeline run in real-time, or you can examine past runs of the pipeline using the dropdown at the upper-left of the page. We can open an event log in the bottom pane of this page:
# MAGIC
# MAGIC 3. At the top of the bottom pane, on the right side, click ![issues-icon.png](../Includes/images/issues-icon.png "issues-icon.png")
# MAGIC 4. Then, click **View event log**.
# MAGIC
# MAGIC The event log shows you what is going on with the pipeline run from when it was initiated to when it is completed.
# MAGIC
# MAGIC 5. Close the event log by clicking the "X" in the upper-right corner.

# COMMAND ----------

# MAGIC %md
# MAGIC ## View Failed Expectations
# MAGIC We setup three data quality expectations, and we intentionally have some data that fails two of these expectations. Let's look at how we can view the metrics related to our expectations.
# MAGIC
# MAGIC 1. Wait for the pipeline to finish its run.
# MAGIC
# MAGIC Note the three datasets in the graph. These represent our bronze, silver, and gold data. The silver node has a couple of icons in the lower-right corner that show the number of warnings and the number of records dropped.
# MAGIC
# MAGIC 2. Click one of the icons to open the **Expectations** pane.
# MAGIC
# MAGIC We see the two expectations that were violated: *valid_role* and *valid_country*, and there was one record each that violated the expectations. For *valid_role*, the record that violated the expectation was not written to the silver table. For *valid_country*, we are warned that there was a record that violated the expectation, but the record was still written to the table.
# MAGIC
# MAGIC 3. Close the **Expectations** pane by clicking the "X" in the upper-right corner.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Optimize a Pipeline
# MAGIC You have the ability to check individual query metrics for each dataset in the pipeline. This can be useful to diagnose issues with long running queries or to simply improve query performance. Complete the following:
# MAGIC
# MAGIC 1. Click **All tables** in the upper-right of the bottom pane.
# MAGIC 2. Click the **Performance** tab. 
# MAGIC
# MAGIC Note the three queries.
# MAGIC
# MAGIC 3. Click the query that refreshed the bronze table. 
# MAGIC
# MAGIC Along with timing information, we get helpful metrics like the number of row read, the number of bytes read, and whether any data spilled onto disk. Although we don't have time to discuss these metrics in this course, we do have other courses on optimizing Spark that can be very helpful.
# MAGIC
# MAGIC 4. Click **See query profile** at the bottom of the pane.
# MAGIC
# MAGIC We get a graph that displays how the query was executed. Read this from the bottom up.
# MAGIC
# MAGIC 5. Click the bottom node, titled **Scan**.
# MAGIC
# MAGIC We get more information related to the scanning portion of the query where the data was actually read from the source. Among these are some very helpful metrics like the number of files read and the size of files read. Again, these metrics can help us see why queries might be taking longer than they need to be.
