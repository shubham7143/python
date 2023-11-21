# obj: to study acess modifiers(public, protected, private)

class Employee():
    name = ""
    _role = ""
    __salary = ""

    def __init__(self, name, role, salary) -> None:
        self.name = name
        self._role = role
        self.__salary = salary

    def printDetails(self):
        print("Your role is :", self._role)
        print("Your salary is :", self.__salary)


if __name__ == "__main__":
    e1 = Employee("Shubham", "data sciencetist", "12 lakh")
    e1.printDetails()
