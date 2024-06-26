from proj.tasks import AddTask
from proj.helper import makeWorker


class AddTaskImpl(AddTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a + b
        return result

#create celery app
app, _ = makeWorker(AddTaskImpl)

#starts worker
if __name__ == '__main__':
    app.worker_main()

