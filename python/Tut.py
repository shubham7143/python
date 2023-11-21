a, b, c, d = 1, 2, 3, 4

c = 0
for i in range(1, a+1):
    print(i)
    for j in range(1, b+1):
        print(i, j)
        for k in range(1, c+1):
            print(i, j, k)
            for l in range(1, d+1):
                print(i, j, k, l)
                if(i^j^k^l != 0):
                    c += 1
print(c)