#wap to understand decorators and wrapper function.

def inner1(func):
    """This is a decorator function."""
    def inner2():
        """This is a wrapper function."""
        print("Before execution:")
        func()
        print("Execution completed.")
    return inner2

#calling decorator
@inner1
def fun():
    """Function used to decorate:"""
    print("Executing...")
fun()
