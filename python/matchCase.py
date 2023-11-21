x = int(input("Enter First number : "))
y = int(input("Enter Second number : "))

match x + y:
    case 1:
        print("case 1")
    case 2:
        print("case 2")
    case 3:
        print("case 3")
    case _:
        print("default")
