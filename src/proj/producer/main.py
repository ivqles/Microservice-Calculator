import random

from celery_tasks.tasks import AddTask, SubtractTask, MultiplyTask, DivideTask
from celery_tasks.helper import makeWorker
from flask import Flask

flask_app = Flask(__name__)

# create worker
_, addition_worker = makeWorker(AddTask)
_, subtraction_worker = makeWorker(SubtractTask)
_, multiplication_worker = makeWorker(MultiplyTask)
_, division_worker = makeWorker(DivideTask)


@flask_app.route('/create_tasks/<count>')
def create_tasks(count):
    count = int(count)
    for i in range(count):
        num_1 = random.randint(1, 1000)
        num_2 = random.randint(1, 1000)
        addition_worker.apply_async(args=[num_1, num_2 ])
        subtraction_worker.apply_async(args=[num_1, num_2 ])
        multiplication_worker.apply_async(args=[num_1, num_2 ])
        division_worker.apply_async(args=[num_1, num_2 ])
    return "Done " + str(count)


if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port=5001)