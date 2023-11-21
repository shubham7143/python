'''class Animal:
    def speak(self):
        print("Animal speak.")


class Dog(Animal):
    def bark(self):
        print("Dog bark.")


class DogChild(Dog):
    def eat(self):
        print("Eating bread.")


d = DogChild()
d.bark()
d.speak()
d.eat()
'''

'''
class Calculation1:
    def summation(self, a, b):
        return a+b


class Calculation2:
    def multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b


d = Derived()
# print(d.summation(9, 1))
# print(d.multiplication(9, 1))
# print(d.divide(9, 1))
# print(issubclass(Derived, Calculation1))
# print(issubclass(Calculation1, Calculation2))
print(isinstance(d, Calculation1))
'''
