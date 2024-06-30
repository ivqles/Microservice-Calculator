'''
Class Interfaces for Each Microservice Operations
'''

from .celery import celery

# REMOVED: replaced with custom Task classes to allow for definitions to be defined in separate microservice directories
# @celery.Task
# def add(x, y):
#     pass

class AddTask(celery.Task):
    name = 'add'

    def run(self, x, y):
        pass

# REMOVED: all task registering and worker creation intended to be separated into a new function and/or file
# celery = celery.tasks[AddTask.name]

class SubtractTask(celery.Task):
    name = 'subtract'

    def run(self, x, y):
        pass

class MultiplyTask(celery.Task):
    name = 'multiply'

    def run(self, x, y):
        pass

class DivideTask(celery.Task):
    name = 'divide'

    def run(self, x, y):
        pass