# 
# Example file for working with functions
#

# define a basic function 
def func1():
    print("I am basic function")

# function that takes arguments
def func2(func2var1, func2var2):
    print("I'am a " + func2var1 + " that takes " + func2var2)

# function that returns a value
def func3(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range (x):
        result = result * num
    return result

# function with multiple arguments
# when taking a formal argument with the argument list, the arg list should always be the last parameter.
def multiAdd(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1()
# func2("function", "arguments")
# print(func3(8)) 

print(power(10))
print(power(2,3))
print(power(x=4,num=3))
print(multiAdd(4,5,10))
