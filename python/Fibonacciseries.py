#Program to calculate 'n'th term of fibonacci series.

def fib(n):
    '''This function calculates 'n'th term of fibonacci series.'''
    if(n == 1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter n: "))
print("The %dth of fibonacci series is %d." %(n, fib(n)))