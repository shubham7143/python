class Student:
    leaves = 7
    
    #constructor
    def  __init__(self, name, stream) -> None:
        self.name = name
        self.stream = stream

    #method
    def printData(self):
        print(Student.leaves)
        return self.name

    #class methods
    @classmethod
    def myClass(cls, newLeaves):
        cls.leaves = newLeaves

    @classmethod
    def saveData(cls, string):
        '''This is a alternate for a constructor.'''
        # newString = string.split('-')
        # return cls(newString[0], newString[1])
        return cls(*string.split('-'))

if __name__=='__main__':
    s1 = Student("Shubham", "cs-ds")
    s2 = Student.saveData("Sam-cse")
    s1.myClass(10)
    print(s1.printData())
    print(s2.printData())

