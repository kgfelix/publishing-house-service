pre requisites
 - python
 pip


Create a new virtual environment, if it hasn't been created yet: python3 -m venv env;
Activate the virtual env: source env/bin/activate;
Install the dependencies: pip3 install -r requirements.txt


uvicorn app.main:app --reload