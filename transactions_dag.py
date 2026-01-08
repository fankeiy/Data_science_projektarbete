from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append("/home/elias/data_science/automated_data_pipeline")

from src.pipeline import run_pipeline

with DAG(
    dag_id="transactions_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_pipeline_task  = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline
    )
