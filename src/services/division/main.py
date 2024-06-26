from proj.tasks import DivideTask


class DivideTaskImpl(DivideTask):

    def run(self, x, y):
        a = float(x)
        b = float(y)

        result = a / b
        
        if b == 0:
            result = 'undefined'

        return result