from celery import Celery

app = Celery('proj',
             broker='pyamqp://guest@localhost//',
             backend='rpc://',
             include=['proj.tasks'])

if __name__ == '__main__':
    app.start()