from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(dag_id='09_03_file_sensor',
        description='This DAG is used to test the file sensor',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        max_active_runs=1
        ) as dag:

    t1 = BashOperator(task_id='creating_file',
                    bash_command='sleep 10 && touch /tmp/file.txt')

    t2 = FileSensor(task_id='waiting_file',
                    filepath='/tmp/file.txt')

    t3 = BashOperator(task_id='end_task',
                    bash_command='echo "End of the DAG"')

    t1 >> t2 >> t3