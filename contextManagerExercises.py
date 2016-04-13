from datetime import datetime


class NoException:
    def __init__(self, *args):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("ignoring exception:" + str(exc_val))
        return True


class Timed:
    def __init__(self, operation):
        self.operation = operation

    def __enter__(self):
        self.timeTook = datetime.now().microsecond

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.timeTook = datetime.now().microsecond - self.timeTook
        print("%s took %s:" % (self.operation, self.timeTook))


def benchmark():
    with Timed("list comprehension"):
        [str(i) for i in xrange(100000)]
    with Timed("map"):
        map(str, xrange(100000))

if __name__ == "__main__":
    benchmark()
    with NoException([ZeroDivisionError]):
        1 / 0


