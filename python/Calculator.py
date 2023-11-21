#wap to make a calculator.

o = input("Enter operator:\n+\t-\t*\t/\n")
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))

if o=='+':
    print("Sum = ",(a+b))
elif o=='-':
    print("Difference = ",(a-b))
elif o=='*':
    print("Product = ",(a*b))
elif o=='/':
    print("Quotient = ",(a//b))
else :
    print("Invalid operation.")
