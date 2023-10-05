"""
Instance method():
instance method are used to access or modify the object state.instance variables inside a method
is called instancemetod.instance method must have first paramete is self.
"""
class Employee:

    def __init__(self,EmpID,EmpName,gender):
        self.Id = EmpID
        self.name = EmpName
        self.gender = gender

    def show(self):
        print(self.Id,self.name,self.gender)


    def update(self,EmpID,gender):
        self.Id = EmpID
        self.gender = gender


    def add_new(self,location):
        self.location = location


emp1 = Employee(46196090,'Vinod','Male')
emp1.show()
emp1.update('1223690','Female')
emp1.show()
emp1.add_new('Bangalore')


print("Dynamically add instance methods to object")




#types.MethodTypes(method_name,object)

import types
class Car:

    def __init__(self,model,colour,country):
        self.model = model
        self.colour = colour
        self.country = country

    def myfunc(self,contactNo,location):
        self.contact = contactNo
        self.location = location


def details(self):
    print(self.model,self.colour,self.country)

def welcom(self):
    print("Welecome to CarBazar")

def contact_details(self):
    print(self.contact,self.location)





c1 = Car('XMV7489653','Red','Germany')

c1.details = types.MethodType(details,c1)
c1.details()

c1.welcome = types.MethodType(welcom,c1)
c1.welcome()

c1.myfunc(7569352177,'Bangalore')


c1.contact_details = types.MethodType(contact_details,c1)
c1.contact_details()



string = "Python Programme"

word_count = dict([(x,x.count(x)) for x in string])
print(word_count)


print("dynamically add instance methods to class")
"""
types.MethodType("method_name,object)
"""


class Person:

    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location


    def show(self):
        print("This is instance method")

def details(self):
    print(self.name,self.age,self.location)





p1 = Person('vinod',30,'Bangalore')
p1.details = types.MethodType(details,p1)
p1.details()


print("Dynamically delete instance method")
"""
syntax:
del object_name.method
delatter(object_name,method)

"""
#del p1.show
#p1.show()

#delattr(p1,details)
#p1.details()

