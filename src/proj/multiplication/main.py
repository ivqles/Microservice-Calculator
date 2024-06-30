from celery_tasks.tasks import MultiplyTask
from celery_tasks.helper import makeWorker


class MultiplyTaskImpl(MultiplyTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a * b
        return result

celery, _ = makeWorker(MultiplyTask)

if __name__ == '__main__':
    celery.worker_main()