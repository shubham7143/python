class Student:
    
    #constructor
    def __init__(self, name, stream) -> None:
        self.name = name
        self.stream = stream

    #static method
    @staticmethod
    def printName(string):
        print("My name is", string)

if __name__=='__main__':
    s1 = Student("Shubham", "cs-ds")
    s1.printName("Shubham")