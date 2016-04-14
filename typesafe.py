class TypeSafe(object):

    def __init__(self, datatype):
        self.datatype = datatype
        self.value = 0

    def __set__(self, instance, value):
        if type(value) != self.datatype:
            raise TypeError("Expected %s, got %s" % (self.datatype, type(value)))
        else:
            self.value = value


class Person(object):
    name = TypeSafe(str)
    age = TypeSafe(int)

if __name__ == "__main__":
    p = Person()
    p.name = "Name"
    p.age = 1
    # p.age = "not an int" fails!!
