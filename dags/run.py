from datetime import datetime, timedelta
from airflow.decorators import dag
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy_operator import DummyOperator
from docker.types import Mount


@dag(start_date=datetime(2024, 11, 25), schedule=None, catchup=False)
def airflow_docker_operator():

    start_dag = DummyOperator(
        task_id='start_dag'
    )

    end_dag = DummyOperator(
        task_id='end_dag'
    )    

    writer_task = DockerOperator(
        task_id='write',
        image='writer:v1',
        command="echo 'Im writing'",
        container_name='writer',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        auto_remove=True,
        mounts=[
            Mount(
                source='/home/semyon/airflow/sample-run/data', 
                target='/data', 
                type='bind'
        )]
    )
    
    reader_task = DockerOperator(
        task_id='read',
        image='reader:v1',
        command="echo 'Im reading'",
        container_name='reader',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        auto_remove=True,
        mounts=[
            Mount(
                source='/home/semyon/airflow/sample-run/data', 
                target='/data', 
                type='bind'
        )]
    )
    start_dag >> writer_task >> reader_task >> end_dag


airflow_docker_operator()
