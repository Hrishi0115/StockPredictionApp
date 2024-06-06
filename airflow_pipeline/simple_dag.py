# `/airflow/dags/simple_dag.py`

# This file defines a Directed Acyclic Graph that consists of three tasks:
# 1. `print_date`
# 2. `sleep`
# 3. `templated`

# each uses the `BashOperator` to execute a bash command

# When the DAG is triggered, Airflow executes the tasks in the order defined by their dependencies
# 


from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 6),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'simple_dag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

# Define the tasks
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t3 = BashOperator(
    task_id='templated',
    bash_command='echo "The date today is {{ ds }}"',
    dag=dag,
)

# Set task dependencies
t1 >> t2
t2 >> t3