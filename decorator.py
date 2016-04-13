def log(original_function):
    def function_executor(*args, **kwargs):
        result = original_function(*args, **kwargs)

        with open('log.txt', 'a') as f:
            f.write("Invoked method %s with args as %s and kwargs as %s returned result:%s"
                    % (original_function.__name__, args, kwargs, result))
        return result
    return function_executor


@log
def add(x, y):
    return x + y

if __name__ == "__main__":
    print(add(2, 3))
