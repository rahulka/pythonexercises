class CaseInsensitive(object):

    def __init__(self):
        pass

    def __getattr__(self, item):
        print("Getting attr:" + str(item))
        result = 0
        try:
            result = self.__dict__[str(item).lower()]
        except KeyError:
            result = self.__dict__[str(item).upper()]

        return result

if __name__ == "__main__":
    obj = CaseInsensitive()
    obj.A = "asd"
    print(obj.a)
    print(obj.A)
