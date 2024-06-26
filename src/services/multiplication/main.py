from proj.tasks import MultiplyTask


class MultiplyTaskImpl(MultiplyTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a * b
        return result