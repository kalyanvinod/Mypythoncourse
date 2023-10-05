"""
what is namespace?


what is scope?

local scope:
A local scope refers to the objects available in the current function.

global scope:
A global scope refer to a object availble  througt the code.

"""

x = 'global scope x'
def test():
    global  x
    x = "local scope  x"
    #print(y)
    #Accessing global variable inside function
    print(x)
test()
#Accessing local variable outside the function
print(x)



