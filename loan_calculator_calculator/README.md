# Loan Calculator Web App

This project is built using Django, Gunicorn, VueJS, Docker and docker-compose.

## Project setup
```
Clone/unpack this repository
Install Docker and docker-copose utilities (please, visit official web-site for download and installation instructions)
```

## Run Project
Please, go into the root of this project and run the following command
```
docker-compose up
```

## Need to re-build

Run in the root of the project
```
docker-compose build
```

## Run tests
To run the tests one needs an environment. Please, choose by your preference:
 - Docker environment
 - python virtual environment

## Virtual Environment
If virtual environment is what you'd like to move forward with , then:
```
pip install virtualenv
virtualenv [directory_path/directory_name]
```
then run activate script in Windows:
```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```
or in Linux:
```
$ source myvenv/bin/activate
```
After that please, run ``pip install -r requirements.txt`` - Now you are ready to run tests.