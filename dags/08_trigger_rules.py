from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime

default_args = {}

def myfunction():
        raise Exception

dag = DAG(dag_id='trigger_rules',
        description='This DAG is used to test the trigger rules between tasks',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        default_args=default_args,
        max_active_runs=1
        )

task1 = BashOperator(task_id='task1',
                bash_command='sleep 5 && echo "Task 1"',
                retries=2,
                retry_delay=5,
                trigger_rule=TriggerRule.ALL_SUCCESS,
                depends_on_past=False,
                dag=dag)

task2 = BashOperator(task_id='task2',
                bash_command='sleep 5 && echo "Task 2"',
                retries=2,
                retry_delay=5,
                trigger_rule=TriggerRule.ALL_SUCCESS,
                depends_on_past=True,
                dag=dag)

task3 = BashOperator(task_id='task3',
                bash_command='sleep 5 && echo "Task 3"',
                retries=2,
                retry_delay=5,
                trigger_rule=TriggerRule.ALWAYS,
                depends_on_past=True,
                dag=dag)

task4 = PythonOperator(task_id='task4',
                python_callable=myfunction,
                retries=2,
                retry_delay=5,
                trigger_rule=TriggerRule.ALL_SUCCESS,
                depends_on_past=True,
                dag=dag)

task5 = BashOperator(task_id='task5',
                bash_command='sleep 5 && echo "Task 5"',
                retries=2,
                retry_delay=5,
                depends_on_past=True,
                dag=dag)

task1 >> task2 >> task3 >> task4 >> task5

