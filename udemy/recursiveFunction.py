def addOrFactorial(num, par):
    if (par == 0):
        res = add(num)
    elif (par == 1):
        res = fact(num)
    else:
        res = -1
    return res


def add(num):
    if (num == 0):
        return 0
    else:
        return num + add(num-1)


def fact(num):
    if (num == 1):
        return 1
    else:
        return num * fact(num-1)


print(addOrFactorial(5, 2))
