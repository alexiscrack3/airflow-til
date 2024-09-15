
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import datetime

dag = DAG(dag_id='09_02_external_sensor',
        description='This DAG is used to test the sensor operator',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        max_active_runs=1
        )

t1 = ExternalTaskSensor(task_id='waiting_dag',
    external_dag_id='09_01_external_sensor',
    external_task_id='the_task',
    poke_interval=10,
    dag=dag)

t2 = BashOperator(task_id='task2',
                bash_command='sleep 10 && echo "Task 2"',
                depends_on_past=True,
                dag=dag)

t1 >> t2