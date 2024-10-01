from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator
from datetime import date

default_args = {
    'start_date': datetime(2024, 9, 1),
    'end_date': datetime(2024, 9, 30),
}

def my_function(**context):
    if context['logical_date'].date() < date(2024, 9, 15):
        return 'task2'

    return 'task3'

with DAG(dag_id='12_branch_operator',
        description='This DAG is used to test branch operator',
        schedule_interval='@daily',
        default_args=default_args,
        ) as dag:

    branch_task = BranchPythonOperator(task_id='branch_task',
                    python_callable=my_function)

    t2 = BashOperator(task_id='task2',
                    bash_command='echo "Running {{ds}}"')

    t3 = BashOperator(task_id='task3',
                    bash_command='echo "Running {{ds}}"')

    branch_task >> [t2, t3]