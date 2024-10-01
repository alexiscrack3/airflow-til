from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def my_function(**context):
    val = context['ti'].xcom_pull(task_ids='task2')
    print(int(val) * 2)

with DAG(dag_id='11_xcoms',
        description='This DAG is used to test xcoms',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        max_active_runs=1
        ) as dag:

    t1 = BashOperator(task_id='task1',
                    bash_command='sleep 5 && echo $((3 * 10))')

    t2 = BashOperator(task_id='task2',
                    bash_command='sleep 3 && echo {{ ti.xcom_pull(task_ids="task1") }}')

    t3 = PythonOperator(task_id='task3',
                    python_callable=my_function)

    t1 >> t2 >> t3