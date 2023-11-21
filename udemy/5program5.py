physics = int(input("Enter physics marks:"))
maths = int(input("Enter maths marks:"))
'''
if (physics == maths):
    print("physics marks are equal to maths marks.")
if (physics > maths):
    print("physics marks are greater than maths maks.")
if (maths > physics):
    print("maths marks are greater than physics marks.")
'''
# Better way to write above program
if (physics == maths):
    print("physics marks are equal to maths marks.")
elif (physics > maths):
    print("physics marks are greater than maths maks.")
else:
    print("maths marks are greater than physics marks.")
