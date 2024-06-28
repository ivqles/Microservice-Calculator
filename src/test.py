import random
from flask import Flask
from proj.helper import makeWorker
from proj.tasks import AddTask, SubtractTask, MultiplyTask, DivideTask

app = Flask(__name__)

addition_worker = makeWorker(AddTask)
subtraction_worker = makeWorker(SubtractTask)
multiplication_worker = makeWorker(MultiplyTask)
division_worker = makeWorker(DivideTask)

@app.route("/create_tasks/<count>")
def create_tasks(count):
    count = int(count)
    for i in range(count):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        addition_worker.apply_async(args=(x, y))
        subtraction_worker.apply_async(args=(x, y))
        multiplication_worker.apply_async(args=(x, y))
        division_worker.apply_async(args=(x, y))
    return "Done " + str(count)

if __name__== '__main__':
    app.run(host="0.0.0.0", port=5001)