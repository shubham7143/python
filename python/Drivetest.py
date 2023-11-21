#wap to test that a person is eligible to drive or not.

age = int(input("Enter your age:"))
if (age<0 or age>90):
    print("invalid age.")
elif (age>18):
    print("You can drive.")
elif (age<18):
    print("You cann't drive.")
else :
    print("Can't decide, come for a driving test.")