from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(dag_id='monitoring',
        description='This DAG is used to test the orchestration between tasks',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        default_args={'depends_on_past': True},
        max_active_runs=1
        )

task1 = BashOperator(task_id='task1',
                bash_command='echo "Task 1"',
                dag=dag)

task2 = BashOperator(task_id='task2',
                bash_command='echo "Task 2"',
                dag=dag)

task3 = BashOperator(task_id='task3',
                bash_command='echo "Task 3',
                dag=dag)

task4 = BashOperator(task_id='task4',
                bash_command='echo "Task 4"',
                dag=dag)

task1 >> task2 >> [task3, task4]

