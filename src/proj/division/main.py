from celery_tasks.tasks import DivideTask
from celery_tasks.helper import makeWorker

class DivideTaskImpl(DivideTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a / b
        
        if b == 0:
            result = 'undefined'

        return result

celery, _ = makeWorker(DivideTask)

if __name__ == '__main__':
    celery.worker_main()