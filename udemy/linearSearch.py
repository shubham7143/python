def linearsearch(numbers, num):
    for idx in range(len(numbers)):
        if (numbers[idx] == num):
            return idx
    else:
        return -1


numbers = [12, 33, 35, 56, 67, 98]
num = 35
print(linearsearch(numbers, num))
