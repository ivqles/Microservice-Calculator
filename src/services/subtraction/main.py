from proj.tasks import SubtractTask


class SubtractTaskImpl(SubtractTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a - b
        return result