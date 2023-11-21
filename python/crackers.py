arr = [1, 2, 3]
crakers = 7
rem = crakers%sum(arr)
i = 0
while(arr[i] <= rem):
    rem -= arr[i]
    i += 1
if(rem == 0):
    print("yes")
else:
    print("no", rem)