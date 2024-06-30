from celery_tasks.tasks import AddTask
from celery_tasks.helper import makeWorker


class AddTaskImpl(AddTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a + b
        return result

celery, _ = makeWorker(AddTask)

if __name__ == '__main__':
    celery.worker_main()