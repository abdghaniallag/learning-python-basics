#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def functionOne():
    print("functionOne")

# TODO: function that takes arguments
def functionTwo(argumentOne ,argumentTwo ):
    print(argumentOne+argumentOne)


# TODO: function that returns a value
def cube(x=1):
    return x*x*x


# TODO: function with default value for an argument
def power(number , x=1):
    result=1;
    for i in range(x):
        result=result*number
    return result

# TODO: function with variable number of arguments
def multiAdd(*args):
    result =0
    for i in args:
        result = result + i
    return result

functionOne()
print(functionTwo("arfsv","arsgfwedsf "))
print(multiAdd(4,8,8,8,7))