import subprocess
import fileinput
import os

# This is required since we don't process GitHub actions
project_slug = '{{ cookiecutter.project_slug }}'
filename = os.path.join('.github', 'workflows', 'release-please.yml')
with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace('project_slug', project_slug), end='')


subprocess.call(['git', 'init'])
subprocess.call(['npm', 'install'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'chore: initial commit'])
