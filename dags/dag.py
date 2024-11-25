from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'docker_sequence_dag',
    default_args=default_args,
    description='A sequence of tasks running in Docker containers',
    schedule_interval=None,
)

# Задача 1
task_1 = DockerOperator(
    task_id='task_1',
    image='your_docker_image_1',
    api_version='auto',
    auto_remove=True,
    command='/bin/bash -c "echo Task 1"',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Задача 2
task_2 = DockerOperator(
    task_id='task_2',
    image='your_docker_image_2',
    api_version='auto',
    auto_remove=True,
    command='/bin/bash -c "echo Task 2"',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Задача 3
task_3 = DockerOperator(
    task_id='task_3',
    image='your_docker_image_3',
    api_version='auto',
    auto_remove=True,
    command='/bin/bash -c "echo Task 3"',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag,
)

# Определение последовательности задач
task_1 >> task_2 >> task_3
