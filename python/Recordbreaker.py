# kickstart: calculate no. of record breaker days.

def recordBreaker(n, lov):
    list1 = []
    count = 0
    for i, visitor in enumerate(lov):
        if (i == 0 or max(list1) < visitor):
            if (i == n-1 or (visitor > lov[i+1])):
                count += 1
                #print(count, i)
        list1.append(visitor)

    return count


t = int(input())
listOfVisitors = []
for i in range(t):
    n = int(input())
    listOfVisitors = list(map(int, input().split()))
    count = recordBreaker(n, listOfVisitors)
    print(f"Case #{i+1}: {count}")
