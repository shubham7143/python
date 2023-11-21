#Take a number ask user to guess it in 7 attempts .

n = 18
i = 0

while (i<7):
    inp = int(input("Guess the number: "))
    i = i+1
    if(inp == n):
        print("Congratulions you guessed the correct number in %d attempts."% (i))
        break
    elif(inp > n):
        print("You entered larger number.\n%d attepts left."%(7-i))
    elif(inp < n):
        print("You entered smaller number.\n%d attempts left."%(7-i))

if(i>7):
    print("max attempts reached\nGame over.")