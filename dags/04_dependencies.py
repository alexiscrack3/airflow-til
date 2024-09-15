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

t1 = PythonOperator(task_id='task1',
                        python_callable=print_hello,
                        dag=dag)

t2= BashOperator(task_id='task2',
                    bash_command='echo "Task 2"',
                    dag=dag)

t3 = BashOperator(task_id='task3',
                    bash_command='echo "Task 3"',
                    dag=dag)

t4 = BashOperator(task_id='task4',
                    bash_command='echo "Task 4"',
                    dag=dag)

# t1.set_downstream(t2)
# t2.set_downstream([t3, t4])
t1 >> t2 >> [t3, t4]

