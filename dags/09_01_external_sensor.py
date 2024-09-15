
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(dag_id='09_01_external_sensor',
        description='This DAG is used to test the sensor operator',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        max_active_runs=1
        )

t1 = BashOperator(task_id='the_task',
                bash_command='sleep 10 && echo "Task 1"',
                depends_on_past=True,
                dag=dag)
t1