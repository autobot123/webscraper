import subprocess
import sys


def install_module(module_name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_name])
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])


### SCRIPT ###

python_modules = 'selenium,spacy,pytest,pandas,argparse'
python_modules_list = python_modules.split(",")

for module_name in python_modules_list:
    install_module(module_name)
