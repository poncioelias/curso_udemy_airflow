from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from big_data_operator import BigDataOperator


dag = DAG('bigdata', description="Nossa primeira Dag usando plugin",
          schedule_interval=None, start_date=datetime(2023,3,5),catchup=False)


big_data = BigDataOperator(
    task_id='big_data',
    path_to_csv_file='/opt/airflow/data/Churn.csv',
    path_to_save_file='/opt/airflow/data/Churn.parquet',
    file_type='parquet',
    dag=dag
)

big_data