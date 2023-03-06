import os
import yaml

for subdir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.yaml'):
            print(os.path.join(subdir, file))
