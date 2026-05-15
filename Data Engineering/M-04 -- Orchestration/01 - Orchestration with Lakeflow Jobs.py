# Databricks notebook source
# MAGIC %md
# MAGIC ![databricks_academy_logo.png](../Includes/images/databricks_academy_logo.png "databricks_academy_logo.png")

# COMMAND ----------

# MAGIC %md
# MAGIC # Orchestration with Lakeflow Jobs
# MAGIC
# MAGIC Let’s explore unified orchestration with Databricks using Lakeflow Jobs for end to end platform-wide orchestration.
# MAGIC
# MAGIC ### Unified Orchestration in Databricks
# MAGIC ![get_started_de_lakeflow_jobs_ui.png](../Includes/images/get_started_de_lakeflow_jobs_ui.png)
# MAGIC Fully-managed cloud-based general-purpose task orchestration service for the entire platform.
# MAGIC For data engineers, data scientists and analysts to build reliable data, analytics and AI Lakeflow Jobs using Notebooks, Jobs for SQL, ML models and more.
# MAGIC Easy to use point-and-click interface.
# MAGIC Lakeflow Spark Declarative Pipelines can be a task in a Lakeflow Job.
# MAGIC
# MAGIC
# MAGIC Lakeflow Jobs is a fully-managed, cloud-based, general-purpose task orchestration service for the entire platform. It removes operational overhead with a fully managed orchestration service enabling you to focus on your Jobs, not on managing your infrastructure. 
# MAGIC Lakeflow Jobs is a service for anyone in the organization, including data engineers, data scientists and analysts, allowing them to build reliable data, analytics and AI Lakeflow Jobs on any cloud. Data teams can orchestrate any combination of tasks, such as notebooks, SQL, ML models python code, as well as Spark Declarative pipelines. 
# MAGIC Your team can easily create, run, monitor and repair data pipelines without managing any infrastructure. With an easy point-and-click authoring experience for all your data teams not just those with specialized skills, Lakeflow Jobs makes it easy to author and execute orchestrated workloads.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Building Blocks of a Lakeflow Job
# MAGIC
# MAGIC ![get_started_de_lakeflow_job_blocks.png](../Includes/images/get_started_de_lakeflow_job_blocks.png)
# MAGIC
# MAGIC Building a Lakeflow Job begins with considering the the type of task you want to complete. Then you can define how that task should be executed in the control flow. Finally, you define the type of trigger trigger necessary to kick off the job. Databricks offers several different options to make building Lakeflow Jobs simple and convenient for all users.  
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Actionable insights from real-time monitoring
# MAGIC
# MAGIC ![get_started_de_lakeflow_job_monitoring.png](../Includes/images/get_started_de_lakeflow_job_monitoring.png)
# MAGIC
# MAGIC The deep integration of Lakeflow Jobs with the the platform means you get full, deep observability to every job that is running. Monitoring visualization helps you get a quick view of everything that is running and a drill down allows you to troubleshoot issues quickly 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Timeline view with query insights
# MAGIC Improved Observability for job runs
# MAGIC
# MAGIC ![get_started_de_lakeflow_job_query_insights.png](../Includes/images/get_started_de_lakeflow_job_query_insights.png)
# MAGIC
# MAGIC Observibility remains an important part of Databricks Lakeflow Jobs and we continuously invest in bringing more experiences that allow our customers to get actionable insights regarding their workloads and how each job runs. 
# MAGIC
# MAGIC We have added an exciting new visualization to Lakeflow Jobs which is especially useful for non-trivial jobs with multiple tasks. 
# MAGIC
# MAGIC This Gantt view lets you see each job run with the various dependencies and you’ll be able to easily identify which tasks in a job run slowly and where you might have opportunities to optimize.
# MAGIC
# MAGIC
