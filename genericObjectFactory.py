
class GenericObjectFactory:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        output = self.__class__.__name__
        output += ": " +", ".join(["%s=%s" % (k,v) for k,v in self.__dict__.items()])
        return output

if __name__ == "__main__":
    dict = {"a": "1", "b": 2}
    factory = GenericObjectFactory(**dict)
    print(factory)

