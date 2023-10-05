"""
what is class?
class is user-defined data structure that bindes data members and method in single unit.
class is blue print of object creation.using class we can create as many objects we want.

what is object?
object is instance of class.it is collection of variables and method. we can use object class
to perform actions.

identity:
every object must be uniqly identified.
state:
an object has attributes that represents state of objects.
behaviour:
an objects has methods that represent behaviour of object.

self in python:
when working with the clasess in the instance methods self is extra first paramenter.
dont need to pass value for the self parameter by default python provide value for it.
The self parameter refer to the instance of class that is currently being is used.


constructor in python:
when working with class the class containe constructor it is special method named __init__
it get calld when the instace of class is created.this method is used to intilize attributes of the object.

Types of constructor:
default constructor


parametaraized constructor
syntax:
def __init__(self,var1,var2....varn)


non parametaraized constructor
syntax:
def __init__()

"""
class Person:
    def __init__(self,name,age,gender):
        #data members or attributes
        self.name = name
        self.age = age
        self.gender = gender
    def details(self):
        print("Name of student:",self.name)
        print("Age:",self.age)
        print("gender:",self.gender)

    def print_name(self):
        print(self.name)





obj = Person('vinod',30,'Male')
obj.details()

print("Example for non-parameterized constructor")

class Student:
    def __init__(self):
        self.name = 'vinod'
        self.comapany = 'capgemini'

    def details(self):
        print(self.name)
        print(self.comapany)

s1 = Student()
s1.details()

print("COnstructor with defualt values")

class Person:

    def __init__(self,name,state='Karnataka',location='Bangalore'):
        self.name = name
        self.state = state
        self.location = location

    def show(self):
        print(self.state,self.location)

p  = Person('vinod','Hyderabad')
print(p.name)
p.show()



"""
Instance variables:
Instance variables are variabels that are defined inside constructor or instance methods.
this variables varies for object to object.every object has its own copy of instance variables.

"""

class Student:

    def __init__(self,name,age):
        #instance variable
        self.name = name
        self.age = age

    def show(self):
        #instance variables
        print(self.name)
        print(self.age)

s1 = Student('vinod',30)
s1.show()

print("Modifying instance variables")
s1.name = "Suvarna"
s1.age = 29
s1.show()

print("Ways to access instance variables")
"""
instance variables can access with in class and its instance method.
getattr(object,'instace_variable')
getatter(object,instance variable)
"""
print(getattr(s1,'name'))
print(getattr(s1,'age'))

print("Dynamically add instance variables")

s1.Marks = 75
print(s1.name ,s1.age,s1.Marks)

s2 = Student('Pawan kalyan',52)
s2.proffession = "Acting"
print(s2.name,s2.age,s2.proffession)
s2.proffession = "Teching"
print(s2.name,s2.age,s2.proffession)


print("Dynamically delet instace variables")
del s1.name
del s2.proffession
#print(s1.name)
#print(s2.proffession)

delattr(s2,'age')
#print(s2.age)

"""
class variables:
class variables are variables that are defined inside class  outside of any instance method.
class variables shared by all instances of class.
"""
print("Example for class variables")
class Person:
    company = "XYZ business private limited"

    def __init__(self,EmpID,EmpName,role):
        self.EmpId = EmpID
        self.Name = EmpName
        self.role = role

    def details(self):
        #accessing class variables inside instance method
        print(self.Name + " is working in "+ self.company)
        print(Person.company + " is Employee ID is: ",+ self.EmpId)

p = Person(46196090,'Vinod','Python')
p.details()
#accessing class varibales using object reference
print(p.company)
#accessing class variables outside of class
print(Person.company)

print("Modifying class variables")
Person.company = "ABC Business india pvt ltd"

p.details()
print(p.company)
print(Person.company)


