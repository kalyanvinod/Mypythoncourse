"""
class methods:
class methods are used to access to modify class state.in method implementation use class variable such
types  methods are callled class methods. class method are defined using @classmethod  decorator.
its takes cls parameter.

"""
class A:

    def __init__(self):
        print("This is constructor")

    def instance_method(self):
        print("This is classmethod")

    @classmethod
    def class_method(cls):
        print("This is class method")


a1 = A()
a1.instance_method()
a1.class_method()


print("Example for class methods")
class Student:

    school_name = "ABC school"

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def details(self):
        print(self.name + " gender is "+self.gender)


    @classmethod
    def cls_method(cls,year):
        cls.year = year
        print("Joined year is:",cls.year)



s1 = Student("Vinod",30,'Male')
s1.details()

s1.cls_method(2022)


print("Example for Class method")
from datetime import date

class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls,name,birth_year):
        return cls(name,date.today().year - birth_year)


    def show(self):
        print(self.name +"age of student is "+str(self.age))


vinod = Student('vinod',30)
vinod.show()


s2 = Student.calculate_age('vinod',1994)
s2.show()



class MathOperations:

    @classmethod
    def add(cls,a,b):
        return a + b


    @classmethod
    def substract(cls,a,b):
        return a-b

    @classmethod
    def division(cls,a,b):
        return a//b

    @classmethod
    def multiply(cls,a,b):
        return a*b

a = MathOperations()
print("Addition",a.add(5,8))
print(a.substract(100,45))
print(a.division(45,8))
print(a.multiply(8,9))


result1 = MathOperations.add(7,12)
result2 = MathOperations.multiply(5,65)
print(result1,result2)

print("Access class variables using class methods")
class Student:

    school_name = "ABC school"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls,school_name):
        cls.school_name = school_name


    def show(self):
        print(self.name + " school name is "+ Student.school_name)


s1 = Student('Lahari',15)
s1.show()



Student.change_school('XYZ school')
s1.show()

s2 = Student('manoj',14)
Student.change_school('Navodaya school')
s2.show()



class Myclass:

    cls_variable = 15

    @classmethod
    def new_variable(cls,new_value):
        cls.cls_variable = new_value
        return  new_value

value = Myclass.new_variable(25)
print(value)


class Myclass:

    cls_variable = 10


    @classmethod
    def increment_cls_variable(cls):
        cls.cls_variable = cls.cls_variable + 1


Myclass.increment_cls_variable()
Myclass.increment_cls_variable()
Myclass.increment_cls_variable()
print(Myclass.cls_variable)


print("Reverse a string using class and classmethods")

class Newclass:

    word = "Python Developer"

    @classmethod
    def myword(cls):
        return cls.word[::-1]

    @classmethod
    def new_word(cls,text):
        return text[::-1]



rev_word = Newclass.myword()
print(rev_word)

x = Newclass.new_word('Karnati vinod')
print(x)

