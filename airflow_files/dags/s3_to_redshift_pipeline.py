import datetime
import logging

from airflow import DAG
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

import modules.sql_statements as sql_statements 
##### ------ Define python function -------
def load_data_to_redshift(*args, **kwargs):
    """
    Function to load data from s3 to redshift using the copy command
    """
    aws_hook = AwsHook("aws_credentials") #from Step 2.2.1. Set up credentials
    credentials = aws_hook.get_credentials()
    redshift_hook = PostgresHook("redshift") #from Step 2.2.2. Set up connection to redshift
    
    logging.info(sql_statements.COPY_ALL_TRIPS_SQL.format(credentials.access_key, credentials.secret_key))
    ## Run the copy command
    redshift_hook.run(sql_statements.COPY_ALL_TRIPS_SQL.format(credentials.access_key, credentials.secret_key))


##### ------ Define dag -------
dag = DAG(
    'data_pipeline_airflow_Redshift',
    start_date = datetime.datetime.now()
)

##### ------ Define tasks -------
# Create table
create_table = PostgresOperator(
    task_id = "create_table",
    dag = dag,
    postgres_conn_id = "redshift",
    sql=sql_statements.CREATE_TRIPS_TABLE_SQL
)
# Traffic analysis
location_traffic_task = PostgresOperator(
    task_id = "calculate_location_traffic",
    dag = dag,
    postgres_conn_id = "redshift",
    sql=sql_statements.LOCATION_TRAFFIC_SQL
)

### --- Task with PythonOperator ---
copy_task = PythonOperator(
    task_id = 'load_from_s3_to_redshift',
    dag = dag,
    python_callable = load_data_to_redshift
)


##### ------ Configure the task dependencies -------
# Task dependencies such that the graph looks like the following:
# create_table -> copy_task -> location_traffic_task

create_table >> copy_task
copy_task >> location_traffic_task