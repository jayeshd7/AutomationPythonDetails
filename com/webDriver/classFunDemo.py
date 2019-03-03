class MyClass:
    name = "jayesh"
    age = "28"


    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sum(self, a, b):
        print(a+b)


x = MyClass("john", 40)
print(x.name)
x.sum(4, 5)


