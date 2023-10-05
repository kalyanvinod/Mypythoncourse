"""
static methods:
in python ,static method are method that are belongs to class rather than the instance of class.
unlike regular methods, static method are do not operate on instanc specific date and do not access
to the instance attributes and methods. they are asscocicate with the class and the called with out creating the class.

static methods are defined using static method decorator by add this @static method
static methods do not have access  to the instance attributes it does not have in extra first parameters
and also static methods cannot access class level atributes directly.if we need access to class attributes
use class name instead.

"""

class A:

    #static method without parameter
    @staticmethod
    def static_method():
        pass


    #static methods with parameters
    @staticmethod
    def stati_method(var1,var2,var):
        pass



print("Example for static methods")

class Myclass:

    @staticmethod
    def add(x,y):
        return x + y

    @staticmethod
    def substract(x , y):
        return x - y

addition = Myclass.add(3,4)
substact = Myclass.substract(15,9)

print(addition)
print(substact)

print("using static methods for geometric utiles")

class Geometry:

    @staticmethod
    def calculate_area_of_rectangle(length,width):
        return length * width

    @staticmethod
    def calculate_area_of_circle(radius):
        return 3.14 * radius * radius


area_of_rectangle =  Geometry.calculate_area_of_rectangle(25,10)
area_of_circle = Geometry.calculate_area_of_circle(15)
print(area_of_rectangle)
print(area_of_circle)


print("access class variables within static method")
class Myclass:

    cls_name = "ABC School name"

    @staticmethod
    def my_static():
        Myclass.cls_name = "XYZ school"
        print(Myclass.cls_name)

mc = Myclass()
print(Myclass.cls_name)
result = Myclass.my_static()







"""

"""




