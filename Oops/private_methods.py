"""
Private members:
In Python Private methods are methods that are intended for internal use can be accessable within the class
and should not accessable outside of class.protected members are defined prefixing double underscored

"""
print("Example for Private member")

class Myclass:

    def __private_method(self):
        print("This is private method")

    def public_method(self):
        self.__private_method()
        print("This is public method")

class NewClass(Myclass):

    def new_method(self):
        self.__private_method()
        print("This is form another class")

obj = NewClass()
#obj.new_method()

"""
Note:
private members cannot accessable outside of class and its subclass.
"""


class Student:

    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def __validate_age(self):
        return self.__age >= 18

    def eligiblity_check(self):
        if self.__validate_age():
            print("Student Eligible for voting")

        else:
            print("Not Eligible")



stud1 = Student('vinod',25)
stud1.eligiblity_check()

stud2 = Student('suvarna',16)
stud2.eligiblity_check()


"""
Getter and setter methods in python are used to controlle access to an object attributes by providing way 
to get and set their values.use getter method to access data member and use the setter method asscess or modify the
data memebers
"""

print("Examples for getter() method")
class Myclass:

    def __init__(self,value):
        self._value = value

    def get_value(self):
        return self._value

    def set_value(self,value):
        self._value = value


obj = Myclass(25)
print(obj.get_value())

obj.set_value(50)
print(obj.get_value())


class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self,new_age):
        if new_age >= 18:
            self.age = new_age
        else:
            print("Invalid age")

student = Student('Alice',20)
print(f"Student age is: {student.get_age()}")

student.set_age(32)
print(f"Student age is: {student.get_age()}")
