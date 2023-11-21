#while loop.
'''
if __name__=="__main__":
    count = 1
    while(True):
        print("Count :", count)
        count = count+1
        if(count == 4):
            break'''

'''count = 101 
while(True):
    if(count%90==0):
        break
    print("count =", count)
    count += 1'''

# for ch in "Kanpur":
#     print(ch)
#the no of times loop runs is called life of loop.

'''words = ["India", "Japan", "Russia"]
for w in words:
    print(w, len(w))'''

#wap to count no. of vowels.
'''string = input("Enter a string: ")
vowel = ('A', 'E', 'I', 'O', 'U')
count = 0
for i in string:
    if(i in vowel):
        count +=1

print(count)'''

#wap to count no. of consonants in a string.
'''string = input("Enter a string in caps: ")
vowel = ('A', 'E', 'I', 'O', 'U')
count = 0
for i in string:
    if(i not in vowel):
        count +=1

print(count)'''

# print(list(range(1, 6)))
# print(list(range(6)))

'''arr = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(arr)):
    print(i, "=", arr[i])'''

#make an list & append elements find largest element.
'''arr = []
print("Before:", arr)

while(True):
    s1 = input("Enter any name: ")
    arr.append(s1)
    choice = input("wish to add more?(y/n): ")
    if(choice != 'y'):
        break

print("After:", arr)

print(max(arr))'''

#print those name from list whose length is >4.
'''arr = []
print("Before:", arr)

while(True):
    s1 = input("Enter any name: ")
    arr.append(s1)
    choice = input("wish to add more?(y/n): ")
    if(choice != 'y'):
        break

for item in arr:
    if(len(item)>3):
        print(item)'''

#enumerate fn.
'''arr = ['Mary', 'had', 'a', 'little', 'lamb']
print(enumerate(arr))
print(list(enumerate(arr)))
print(tuple(enumerate(arr)))'''

