from proj.tasks import AddTask
from proj.helper import makeWorker


class AddTaskImpl(AddTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a + b
        return result

celery, _ = makeWorker(AddTask)

if __name__ == '__main__':
    celery.worker_main()