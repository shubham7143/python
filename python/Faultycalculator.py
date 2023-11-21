#wap to make faulty a calculator.

o = input("Enter operator:\n+\t-\t*\t/\n")
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

# 45*3 = 555, 56+9 = 77, 56/6 = 4

if (o=='+'):
    if (a==56 and b==9):
        print("Sum = 77")
    elif (a==9 and b==56):
        print("Sum = 77")
    else :
        print("Sum = ",(a+b))
elif (o=='-'):
    print("Difference = ",(a-b))
elif (o=='*'):
    if (a==45 and b==3):
        print("Product = 555")
    elif (a==3 and b==45):
        print("Product = 555")
    else :
        print("Product = ",(a*b))
elif (o=='/'):
    if(a==56 and b==6):
        print("Quotient = 4")
    else :
        print("Quotient = ",(a//b))
else :
    print("Invalid operator.")