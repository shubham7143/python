'''
y = 10
def inner():
    x = 4
    global y
    y = 5
    print(x)
    print("inside the function y:", y)
print("y:", y)
inner()
print("y:", y)

y = 10
def outer():
    z = 15
    def inner():
        x = 4
        nonlocal z
        z = z+1
        print("x:", x)
        print("inside the function z:", z)
    inner()
    print("z:", z)
outer()
'''
