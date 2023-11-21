#wap to calculate fatorial of a number.
def fact(n):
    '''This function calculate of n'''
    if(n == 1):
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter number: "))
#print(fact.__doc__)
print("Factorial of %d is %d."%(n, fact(n)))