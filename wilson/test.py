import os
import yaml

# Define the template for the Python file
PY_TEMPLATE = """\
from dagfactory import DAGFactory

# Define the DAG here
dag = DAGFactory.create_dag({yaml_contents})
"""

airflow_path = '/opt/airflow/dags/repo/pipeline/'

dag_py_folder = 'dag_py_folder'

for subdir, dirs, files in os.walk('.'):
    print('==========')
    print('subdir', subdir)
    for file in files:
        if file.endswith('.yaml'):
            with open(os.path.join(subdir, file), 'r') as f:
                yaml_contents = yaml.load(f, Loader=yaml.FullLoader)
            airflow_yaml_path = os.path.join(airflow_path, subdir, file)
            print(airflow_yaml_path)
