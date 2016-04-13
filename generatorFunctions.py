def count_down(n):
    i = n
    while i > 0:
        yield i
        i -= 1


if __name__ == "__main__":
    for x in count_down(4):
        print(x)
