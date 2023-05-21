# Hello world

# Declare a variable and initialize it
f = 0
# print(f)


# re-declaring the variable works
# f = "abc"
# print(f)

# ERROR: variables of different types cannot be combined
# print("This is a string " + str(12))

# print("This is a string " + 12)

# Global vs Local variables in functions
def someFunction(): 
    # global f #to use global variable in a local scope
    f = "def"
    print(f)

someFunction()
print(f)
