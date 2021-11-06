import subprocess
import sys

python_modules = 'selenium,spacy,pytest,pandas,argparse'
python_modules_list = python_modules.split(",")

for module in python_modules_list:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
