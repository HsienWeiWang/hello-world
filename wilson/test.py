import os
import yaml

# Define the template for the Python file
PY_TEMPLATE = """\
from dagfactory import DAGFactory

# Define the DAG here
dag = DAGFactory.create_dag({yaml_contents})
"""

dag_py_folder = 'dag_py_folder'

for subdir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.yaml'):
            with open(os.path.join(subdir, file), 'r') as f:
                yaml_contents = yaml.load(f, Loader=yaml.FullLoader)

            py_filename = os.path.splitext(file)[0] + '.py'
            py_contents = PY_TEMPLATE.format(yaml_contents=yaml_contents)

            with open(os.path.join(os.getcwd(), dag_py_folder, py_filename), 'w') as f:
                f.write(py_contents)
