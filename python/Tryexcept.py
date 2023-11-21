a = input("Enter 1st number : ")
b = input("Enter 2nd number : ")

try:
    print("Sum of both numbers : ",(int(a)+int(b)))
except Exception as e:
    print("Error!!! only integers allowed\n%s not allowed."%(e))

print("End")