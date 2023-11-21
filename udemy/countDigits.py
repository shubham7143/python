# wap to count no. of digits in  a number.

num = int(input("Enter a num.:"))
count = 0
if (num < 0):
    num = -num
while True:
    if (num >= 1):
        num /= 10
        count += 1
    else:
        break
print("No. of digits :", count)
