from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello World!")

dag = DAG(dag_id='dependencies',
        description='This DAG is used to test the dependencies between tasks',
        start_date=datetime(2024, 1, 1),
        schedule_interval='@once')

task1 = PythonOperator(task_id='task1',
                        python_callable=print_hello,
                        dag=dag)

task2 = BashOperator(task_id='task2',
                    bash_command='echo "Task 2"',
                    dag=dag)

task3 = BashOperator(task_id='task3',
                    bash_command='echo "Task 3"',
                    dag=dag)

task4 = BashOperator(task_id='task4',
                    bash_command='echo "Task 4"',
                    dag=dag)

# task1.set_downstream(task2)
# task2.set_downstream([task3, task4])
task1 >> task2 >> [task3, task4]

