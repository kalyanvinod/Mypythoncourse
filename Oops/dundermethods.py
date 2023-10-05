"""
Dundermethods:
Dundermethods shorts for duble underscoremetods are special methods in python that have
duble underscore at begginging and end of their names.They are also known as magic methods and special methods.
dunder methods are used to define how objects of class behave in certain circumstances or operations.
they are enbles you to custmoize behaviour your classe and instances..


__str__ :This method return string representation when we use str() function and print function.
__repr__:This method return string representation  that can be used to recreate object.

__len__:this method used to customize the behaviour of len() function

"""

print("Examples for dunder methods")

class Myclass:

    def __init__(self,name):
        self.name = name
        self.item = [1,2,4,5,7,8,3]


    #This dunder method return string representation when we use str() and print() function
    def __str__(self):
        return f"Name of the employee is {self.name}"

    def __repr__(self):
        return f"{self.name}"

    def __len__(self):
        return len(self.item)


obj = Myclass('vinod')
print(obj)
print(repr(obj))
print(len(obj.item))



