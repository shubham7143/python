# wap using function to return highest of 3 numbers.

def highestNum(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num3 and num2 > num1):
        return num2
    else:
        return num3


num1, num2, num3 = 12, 79, 18
print(highestNum(num1, num2, num3))
