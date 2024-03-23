import logging

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from 
from airflow.utils import timezone

def _get_dog_api():
    response = request.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    logging.info(data)
    with open("/opt/airflow/dags/dog.json")


with DAG(
    "dog_api_pipeline", #dag_id should be same as filename
    start_date=timezone.datetime(2024, 3, 23),
    schedule="@dairy",
    tags=["DS525"],
):
    start = EmptyOperator(task_id="start")

    get_dog_api = PythonOperator(
        task_id="get_dog_api",
        python_callable=_get_dog_api,
    )

    upload_to_gcs = LocalFilesystemToGCSOperator(
        task_id="upload_to_gcs",
        src=""
    )

    end = EmptyOperator(task_id="end")

    start >> get_dog_api >> end