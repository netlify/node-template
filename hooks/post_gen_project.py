import subprocess

subprocess.call(['git', 'init'])
subprocess.call(['npm', 'install'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
