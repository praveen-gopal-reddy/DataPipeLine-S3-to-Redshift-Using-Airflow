# DataPipeLine-S3-to-Redshift-Using-Airflow

# Overview

In this project, we will looad divvy trips dataset present in S3 to AWS redshift with the help of Airflow and Docker. Divvy is Chicago's bike share system that provides a fast and convenient way to get around without having your own bike
At first we need to finish below tasks

- Build Airflow and Postgres image on docker windows using docker-compose.
- Create Reshift cluster using AWS console.

## Step 1

Build Airflow image using docker-compose

<p align="middle">
  <img src="images/airflow.PNG" />
  
Open Airflow GUI, you will see something like this about datapipeline.

<p align="middle">
  <img src="images/dag.PNG" />

