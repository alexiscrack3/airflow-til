from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from hello_operator import HelloOperator

dag = DAG(dag_id='05_custom_operator',
        description='This DAG is used to test the custom operator',
        start_date=datetime(2024, 1, 1),
        schedule_interval='@once')

t1 = HelloOperator(
    task_id='task1',
    name='World',
    dag=dag)
t1
