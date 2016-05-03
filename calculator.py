from operator import *


def calculator(action, *args):
    result = 0
    result = reduce(action, args)
    return result


if __name__ == "__main__":
    print("Res:" + str(calculator(add, 1, 2, 4)))
    print("Res:" + str(calculator(mul, 1, 2, 4)))
    print("Res:" + str(calculator(sub, 1, 2, 4)))
    print("Res:" + str(calculator(add, 1)))

