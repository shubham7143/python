# wap to calculate factorial of a number.

# Take input from user.
num = int(input("Enter the number, of which you want to calculate the factorial : "))

# logic statements.
if (num < 0):
    print("Sorry, the factorial for negative numbers doesn't exsits.")
elif (num == 0):
    print("The factorial of 0 is : 1")
else:
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print("The factorial of", num, "is", fact, ".")
