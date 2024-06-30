from celery import Celery
from celery_tasks.celery_config import broker_url, backend

# Initiate Celery
celery = Celery('proj',
             broker=broker_url,
             backend=backend,
)

if __name__ == '__main__':
    celery.start()

# Added to README file
# Created Dockerfile and requirements.txt files for: addition, subtraction, multiplication, division
# Created producer file:
    # tried to start flask app in this file but wouldnt work
    # wanted to test out if the workers worked (didn't test yet)
# create test.py to see if the app runs (it doesnt run)
    # it doesnt read proj as a folder
# create config files to connect celery to rabbitMQ
