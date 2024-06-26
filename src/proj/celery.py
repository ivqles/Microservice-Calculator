from celery import Celery

# Initiate Celery
celery = Celery('proj',
             broker='pyamqp://guest@localhost//',
             backend='rpc://',
             include=['proj.tasks'])

if __name__ == '__main__':
    celery.start()