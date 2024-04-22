from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyTableOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator

from airflow.utils import timezone
from datetime import datetime

import os
import json
import csv
import requests

from google.cloud import bigquery
from google.oauth2 import service_account

import logging
from airflow.models import Connection
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


def _get_accident_api():
    api_key = "DQdXFnbDsgMU3QEmQoDM9E1KvECWJNZK"
    headers = {"api-key": api_key}
    params = {"resource_id": "d1ab8a36-c5f7-4efb-b613-63310054b0bc", "limit": 10000}

    response = requests.get("https://opend.data.go.th/get-ckan/datastore_search", params, headers=headers)
    data = response.json()
    records = data.get("result", {}).get("records", [])
    logging.info(records)

    file_path = "/opt/airflow/dags/RoadAccident_2566.csv"
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        # Extract field names from the first record
        fieldnames = records[0].keys() if records else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # Write the header
        writer.writeheader()
        # Write the records
        writer.writerows(records)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': timezone.datetime(2024, 4, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    "accident_api_pipeline",
    default_args=default_args,
    description="A DAG to automate flow: API get JSON file > Write csv file > Send to GCS > Send GCS file to BigQuery",
    schedule="@yearly",
    tags=["DS525"],
)

get_api_file = PythonOperator(
    task_id="get_accident_api",
    python_callable=_get_accident_api,
    dag=dag,
)

upload_to_gcs = LocalFilesystemToGCSOperator(
    task_id="upload_to_gcs",
    src="/opt/airflow/dags/RoadAccident_2566.json",
    dst="RoadAccident_2566.json",
    bucket="swu-ds525-8888",
    gcp_conn_id="my_gcp_conn",
    dag=dag,
)

create_bq_dataset = BigQueryCreateEmptyDatasetOperator(
    task_id='create_dataset',
    dataset_id='proj_accident',  # specify the dataset ID
    project_id='stalwart-summer-413911',  # specify your BigQuery project ID
    location='asia-southeast1',  # specify the location for the dataset
    gcp_conn_id='my_gcp_conn',  # specify the connection ID for GCP
    dag=dag,
)

create_bq_table = BigQueryCreateEmptyTableOperator(
    task_id='create_table',
    dataset_id='proj_accident',  # specify the dataset where you want to create the table
    table_id='accident_case',      # specify the table name
    project_id='stalwart-summer-413911',  # specify your BigQuery project ID
    gcp_conn_id='my_gcp_conn',  # specify the connection ID for GCP
    dag=dag,
)

load_to_bq = GCSToBigQueryOperator(
    task_id='load_to_bq',
    bucket='swu-ds525-8888',
    source_objects=['RoadAccident_2566.csv'],
    destination_project_dataset_table='stalwart-summer-413911.proj_accident.accident_case',
    source_format='CSV',
    create_disposition='CREATE_IF_NEEDED',
    skip_leading_rows=1,  # If CSV has headers
    write_disposition='WRITE_TRUNCATE',  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
    gcp_conn_id="my_gcp_conn",
    dag=dag,
)

get_api_file >> upload_to_gcs >> create_bq_dataset >> create_bq_table >> load_to_bq 