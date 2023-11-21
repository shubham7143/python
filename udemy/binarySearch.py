def binarySearch(numbers, num):
    beg, end = 0, len(numbers)-1
    while (beg <= end):
        mid = (beg + end)//2
        if (numbers[mid] == num):
            return mid
        elif (numbers[mid] < num):
            beg = mid + 1
        else:
            end = mid - 1

    return -1


numbers = [12, 33, 35, 56, 67, 98]
num = 35
print(binarySearch(numbers, num))
