class Student:
    name = ''
    age = ''
    stream = ''

    #constructor
    def __init__(self, name, age, stream):
        self.name = name
        self.age = age
        self.stream = stream

    #methods
    # def saveData(self, name, age, stream):
    #     self.name = name
    #     self.age = age
    #     self.stream = stream

    def printData(self):
        print(self.name)
        print(self.age)
        print(self.stream)
        print()

if __name__=='__main__':
    s1 = Student("Shubham", 19, "cs-ds")
    s2 = Student("Sam", 18, "cse")

    # s1 = Student()
    # s1.saveData("Shubham", 19, "cs-ds")
    
    s1.printData()
    s2.printData()