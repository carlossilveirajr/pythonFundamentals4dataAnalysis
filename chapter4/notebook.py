
# help() shows a man for the object
help(list())

# dir() shows the methods available
ls = ()
dir(ls)

# variable global
_var = 10
def multiply(num1, num2):
    _var = num1 * num2   # create a new local variable
    print(_var)

multiply(10, 2)
print(_var)

"""   it is an error

_var = 10
def multiply(num1, num2):
    _var = _var * num2   # create a new local variable
    print(_var)

multiply(100, 2)
print(_var)
"""


# Variable number of args
def printVarInfo(arg1, *vartuple):
    print("O parametro passado foi: ", arg1)
    for i in vartuple:
        print("O parametro passado foi: ", i)

printVarInfo(10)
printVarInfo(1, 2, 3, 4, 5, 6)

#
# Lambda expression
#


lambda num: num**2 # num^2

par = lambda num: num % 2 == 0

print(par(3))
print(par(6))

reverso = lambda x: x[::-1]
print(reverso("Python"))