from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(dag_id='06_02_orchestration',
        description='This DAG is used to test the orchestration between tasks',
        schedule_interval='0 7 * * 1', # 7 AM every Monday
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        default_args={'depends_on_past': True},
        max_active_runs=1
        )

t1 = BashOperator(task_id='task1',
                bash_command='echo "Task 1"',
                dag=dag)

t2 = BashOperator(task_id='task2',
                bash_command='echo "Task 2"',
                dag=dag)

t3 = BashOperator(task_id='task3',
                bash_command='echo "Task 3"',
                dag=dag)

t4 = BashOperator(task_id='task4',
                bash_command='echo "Task 4"',
                dag=dag)

t1 >> t2 >> [t3, t4]

