'''
Helper Function to register Task Classes
'''

from .celery import celery

def makeWorker(TaskClass, celery_config='proj.celery_config'):
    # check class is valid Task
    assert issubclass(TaskClass, celery.Task)
    celery.config_from_object(celery_config)
    celery.conf.update(task_default_queue=TaskClass.name)
    worker = celery.register_task(TaskClass())

    return celery, worker # returns new updated version of celery and instance of worker task