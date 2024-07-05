from celery import Celery
from celery_tasks.celery_config import broker_url, backend

# Initiate Celery
celery = Celery('proj',
             broker=broker_url,
             backend=backend,
)

if __name__ == '__main__':
    celery.start()
