# Mice test task
Task: develop REST API for table reservation in restaurant.

# Requirements 
- Python >= 3.11
- Docker >= 29.7
- Docker Compose >= 5.5

# Run from source
```bash
git clone git@github.com:guyrilla/mice_task.git # clone this repo

cd mice_task # open project folder

python -m venv .venv # create virtual environment

source .venv/bin/activate # activate virtual environment

python -m pip install -r "requirements.txt" # install python requirements

cd core

uvicorn core.app:entry --reload # start uvicorn server on 127.0.0.1:8000
```
