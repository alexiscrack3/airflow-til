from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(dag_id='bash_operator',
        description="This DAG is used to test the BashOperator",
        start_date=datetime(2024, 1, 1),
        schedule_interval='@once')

t1 = BashOperator(task_id='task1',
                bash_command='echo "Hello World"',
                dag=dag)
t1