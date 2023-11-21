class A:
    def __init__(self, a) -> None:
        self.a = a

    def __add__(self, o):
        return self.a + o.a

obj1 = A(1)
obj2 = A(2)
obj3 = A("hello")
obj4 = A("World")

print(obj1+obj2)
print(obj3+obj4)


class Complex:
    def __init__(self, a, b) -> None:
        self.a = a 
        self.b = b

    def __add__(self, other):
        return self.a+other.a, self.b+other.b


ob1 = Complex(1, 2)
ob2 = Complex(2, 3)
ob3 = ob1 + ob2
print(ob3)