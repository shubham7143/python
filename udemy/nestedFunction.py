def fun():
    # global i
    # i = 10
    print(i)

    def fun1():
        print(20)

    fun1()


i = 30
fun()
print(i)
