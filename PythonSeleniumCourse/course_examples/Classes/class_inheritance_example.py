
class Class1:
    def __init__(self, cl1_inp1):
        print("__init__ of Class 1")
        self.cl1_inp1 = cl1_inp1
        print(self.cl1_inp1)

    def method_1_class_1(self):
        print("method_1_class_1")


class Class2(Class1):
    def __init__(self, cl1inp1, cl2inp1):
        super().__init__(cl1inp1)
        print("__init__ of Class 2")
        self.cl2inp1 = cl2inp1
        print(self.cl2inp1)

    def method_1_class_2(self):
        print("method_1_class_2")


obj2 = Class2('abcd', 'xyz')
obj2.method_1_class_2()

