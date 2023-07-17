# Return multiple values from a function
# Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction.
# Also, it must return both addition and subtraction in a single return call.
# def function(a,b):
#     return print(a+b)
# function(10,80)


# Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
# See: Default arguments in function
# def func(name="Mohit", salary="∞"):
#     name = name
#     salary = salary
#     return print(f"Name : {name}, Salary : {salary}")
# func('abc',10000000)
# func()


# Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it
# and call it using the new name.
# Given:
# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)
# You should be able to call the same function using
# show_student(name, age)
# Hint
# Assign a different name to function using the assignment (=) operator.
# fun_name = new_name
# def display_student(name, age):
#     print(name, age)
# new_name = display_student
# new_name("mohit",21)


# Create a lambda function, that has no parameters, and always return an integer value of 10.
# l = lambda : 10
# print(l())


# Create a lambda function, that has three parameters, and returns the largest of these three
# l = lambda x,y,z : x if x>y and x>z else y if y>z and y>x else z
# print(l(340,54,233))


# Write a program in Python to calculate the value of the following expression by using lambda function.
# The expression is - (x * 10) + (y / 2) * z
# l = lambda x,y,z : (x * 10) + (y / 2) * z
# print(l(1,2,3))


# Write a program to count the number of INTEGERS stored in a list.
# num = [23, 34, 'hello', 32, 56, 234.423]
# f = list(filter(lambda x : x if type(x) == int else '',num))
# print(len(f))