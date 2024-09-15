from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

dag = DAG(dag_id='empty_operator',
        description='This DAG is used to test the EmptyOperator',
        start_date=datetime(2024, 1, 1),
        schedule_interval='@once')

t1 = EmptyOperator(task_id='task1', dag=dag)
t1