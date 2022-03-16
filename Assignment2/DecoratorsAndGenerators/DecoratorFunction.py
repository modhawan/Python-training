def decoratorFunction(func):
    def inner(a, b):
        func(a, b)
        func(a, b)
    return inner

@decoratorFunction
def multiply(a, b):
    print(a*b)

a, b = map(int, input().split(","))
multiply(a,b)
