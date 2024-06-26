import random
from flask import Flask
from proj import workHelper
from proj import AddTask

app = Flask(__name__)

addition_worker = workHelper(AddTask)

@app.route("/")
def create_tasks(count):
    count = int(count)
    for i in range(count):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        addition_worker.apply_async(args=(x, y))
    return "Done " + str(count)

if __name__== '__main__':
    app.run(host="0.0.0.0", port=5000)