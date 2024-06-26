'''
Helper Function to register Task Classes
'''

from .celery import celery

def makeWorker(TaskClass):
    # check class is valid Task
    assert issubclass(TaskClass, celery.Task)
    
    celery.conf.task_default_queue(TaskClass.name)
    worker = celery.register_task(TaskClass())

    return worker