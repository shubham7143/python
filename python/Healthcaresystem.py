#Wap to make a health care system, which saves when & what user has eaten.

def getDate():
    import datetime
    return datetime.datetime.now()

client = {1:"Harry", 2:"Rohan", 3:"Hammmad"}
print("Enter user no.\n1.Harry\n2.Rohan\n3.Hammad")
n = int(input())
print("User%d: %s"%(n,client.get(n)))
print("What you want to do?\n1.log data\n2.retrieve data")
choice = int(input())
if(choice == 1):
    f = open("healthCareSystem.txt", "a")
    print("logging data:")
    print("What you want to log?\n1.Exercise\n2.Diet")
    logChoice = int(input())
    if(logChoice == 1):
        exercise = input("Which exercise you did?\n")
        line = str(getDate())[0:19] + "\t" + client.get(n) + "\t" + exercise + " done"
        f.write(line + "\n") 
    elif(logChoice == 2):
        food = input("What you eat?\n")
        line = str(getDate())[0:19] + "\t" + client.get(n) + "\teat " + food 
        f.write(line + "\n")
    else:
        print("Invalid choice!!!")
    f.close()
elif(choice == 2):
    f = open("healthCareSystem.txt", "r")
    print(f.read())
    f.close()
