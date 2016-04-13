class CountDown:

    def __init__(self, start_from):
        self.counter = start_from

    def __iter__(self):
        return self

    def next(self):
        if self.counter == 0:
            raise StopIteration
        self.counter -= 1
        return self.counter + 1

if __name__ == "__main__":
    cd = CountDown(4)
    for x in cd:
        print(x)