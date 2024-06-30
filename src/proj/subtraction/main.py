from celery_tasks.tasks import SubtractTask
from celery_tasks.helper import makeWorker


class SubtractTaskImpl(SubtractTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a - b
        return result

celery, _ = makeWorker(SubtractTask)

if __name__ == '__main__':
    celery.worker_main()