# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

print("----------------")
def greeting(name):
    def inner():
        print("greet from inner fun",name)
    return inner
g = greeting("nameeee")
g()

print("-----------------")

def outer(func):
    def inner():
        func()
    return inner
def other():
    print("other fun")

x = outer(other)
x()

print("-------------")

def out(funcpass):
    def inner():
        funcpass()
        print("after ...")
    return inner

@out
#use outer fun as decorator
def reusable():
    print("this is reusable")
reusable()

print("--------------")

def smart_divide(func):
    def inner():
        print("before")
        print(func(4,2))
        print("after")
    return inner
@smart_divide
def divide(a,b):
    return a/b
divide()


print("--------------------")

print("CHAINING decorators in python")
def star(func):
    def inner(a,b):
        print([1]*1)
        func(a,b)
        print([2]*2)
        print("aaa")
    return inner

def percent(func):
    def inner(a,b):
        print([3]*3)
        func(a,b)
        print([4]*4)
        print("bbb")
    return inner

@star
@percent
def mult(a,b):
    return print(a*b)
mult(3,3)
