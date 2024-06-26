from proj.tasks import AddTask


class AddTaskImpl(AddTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a + b
        return result