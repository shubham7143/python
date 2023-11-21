#wap to print stars pyramid or inverted pyramid if type == false

n = int(input("Enter no. of rows: "))
type = False
if(type):
    for i in range(1,n+1,):
        for j in range(i):
            print("*",end='')
        print()
else:
    for i in range(n,0,-1):
        print("*"*i)