print("Example for lambda function")

"""
syntax:
lambda arguments : expression
"""
a = lambda x:x**2
print(a(5))

greet = lambda name:"Hello good Morning  " + name
print(greet('Vinod'))


sum = lambda x,y,z:x+y+z
total = sum(10,25,15)
print(total)


print("parameter less lambda funciton")
greet = lambda :print("Hello world")
greet()

even = list(map(lambda x:x%2==0,[1,4,6,5,3,9,8]))

print(even)