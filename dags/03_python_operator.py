from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello World!")

dag = DAG(dag_id='03_python_operator',
        description='This DAG is used to test the PythonOperator',
        start_date=datetime(2024, 1, 1),
        schedule_interval='@once')

t1 = PythonOperator(task_id='task1',
                        python_callable=print_hello,
                        dag=dag)
t1