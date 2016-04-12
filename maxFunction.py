def fmax(*args):
    if len(args) == 0:
        raise Exception("Please pass 1 or more values to calculate values")

    if len(args) == 1:
        return args[0]

    return max(*args)

if __name__ == "__main__":
    print("Max : " + str(fmax(1)))

