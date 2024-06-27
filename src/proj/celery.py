from celery import Celery
from proj.celery_config import broker_url, backend

# Initiate Celery
celery = Celery('proj',
             broker=broker_url,
             backend=backend,
             include=['proj.tasks'])

if __name__ == '__main__':
    celery.start()

# Created Dockerfile and requirements.txt files for: addition, subtraction, multiplication, division
# Created producer file:
    # tried to start flask app in this file but wouldnt work
    # wanted to test out if the workers worked (didn't test yet)
