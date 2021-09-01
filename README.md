# DataPipeLine-S3-to-Redshift-Using-Airflow

# Overview

In this project, we will load divvy trips dataset present in S3 to AWS redshift with the help of Airflow. Divvy is Chicago's bike share system that provides a fast and convenient way to get around without having your own bike.

At first we need to finish below tasks

- Build Airflow and Postgres image on docker windows using docker-compose.
- Create Redshift cluster using AWS console.
- upload divvy trips dataset files [Link to files](https://divvy-tripdata.s3.amazonaws.com/index.html)(pick any year) to S3 bucket. my bucket location is s3://udacity-dend/data-pipelines

## Step 1

### Build Airflow image using docker-compose up command

<p align="middle">
  <img src="images/airflow.PNG" />
  
### Open Airflow GUI, you will see something like this about datapipeline.

<p align="middle">
  <img src="images/dag.PNG" />
  
## Step 2

### Create AWS Redshift cluster using AWS console.
  
<p align="middle">
  <img src="images/cluster-creation-1.PNG" />
  
 <p align="middle">
  <img src="images/cluster-creation-2.PNG" />
   
 ### Cluster Details. 
 
 <p align="middle">
  <img src="images/cluster-creation-1.PNG" />
 
 ### Add cluster permission to read S3 buckets. I have created redshifts3 role as shown below.
   
 <p align="middle">
  <img src="images/cluster-creation-2.PNG" />
   
  <p align="middle">
  <img src="images/create-role-s3.PNG" />
    
 ### final cluster details 
    
 <p align="middle">
  <img src="images/cluster-details.PNG" />
   
## Step 3

### Add AWS and Redshift credentials in Airflow. In aws_credentials, login is your Iam user access key id and password is secret access key.
    
 <p align="middle">
  <img src="images/aws-credentials.PNG" />

### Host is cluster end-point
   
 <p align="middle">
  <img src="images/redshift.PNG" />
 
## Step 4

Switch on the dags in Airflow and verify tables are created in AWS redshift or not.

<p align="middle">
  <img src="images/redshift-tables.PNG" />
  
As you see our divvy trips tables are created in redshift as per sql_statements file which is present in /dags/modules folder
  
## Step 5 
  
### Verfiy the data loaded in redshift tables.
  
<p align="middle">
  <img src="images/data-loaded.PNG" />

