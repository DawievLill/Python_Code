
## With functional abstraction

# def iterativePower(x,p):
#     result = 1
#     for turn in range(p):
#         print ('iteration: ' + str(turn) + ' current result: ' + str(result))
#         result = result * x
#     return result

x = 40

def square(x):
    '''
    x: int or float -- this defines what type of value the input expression is
    '''
    result = x*x
    return result #Shorter would have been to simply say -- return x*x

# squared = square(x)
print ('The square of ' + str(x) + ' is ' + str(square(x))) #You can put the function inside of the print function.
