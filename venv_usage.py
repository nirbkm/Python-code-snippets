# good practice to create venv for each project.

# on new installed machine PS terminal run first to make ps activate external scripts as the venv commands
# not saves configuration!! :'Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force' to be able to activate venvs
# with administrator permissions (runs as admin) 'set-executionpolicy remotesigned'- this will save the configuration

# run in inegrated terminal (currently while writing poweshell with interperted 3.10.2):

# create new venv
# 'python -m venv venvName'
# 'python -m venv venvName --system-site-packages'  this will allow the new env to use system active python version installed packages, that were installed globaly or without activating any env, can be changed manually in venv library, pyvenv.cfg
# activate: 'venvName/Scripts/activate.ps1'
# deactivate: 'deactivate'


# get venv path : 'python  -c "import os; print(os.environ['VIRTUAL_ENV'])"'

# pip list to get packages

# upgrade packages: pip install package_name --upgrade


# to install packages to the main python setup just deactivate env and install with pip
# installing pakcages to the main python setup will avoid to download big packages everytime for each new venv, so big packages just use the system packages


# remove venv
# rm -r venvNamew


import sys

print(sys.path)
