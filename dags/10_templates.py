from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# jinja template
template_command = """
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "File: {{ file }}"
{% endfor %}
"""

with DAG(dag_id='10_templates',
        description='This DAG is used to test the templates',
        schedule_interval='@daily',
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 10, 1),
        max_active_runs=1
        ) as dag:

    t1 = BashOperator(task_id='task1',
                    bash_command=template_command,
                    params={'filenames': ['/tmp/file1.txt', '/tmp/file2.txt']},
                    depends_on_past=True)

    t1