from datetime import datetime
import sys

# Lägg till ditt projekt i PYTHONPATH
sys.path.append("/home/elias/data_science/automated_data_pipeline")

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.pipeline import run_pipeline


default_args = {
    "owner": "elias",
    "depends_on_past": False,
    "retries": 1,
}

with DAG(
    dag_id="automated_data_pipeline",
    default_args=default_args,
    description="Run local data pipeline",
    schedule_interval=None,  # körs manuellt
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    run_pipeline_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_pipeline,
    )
