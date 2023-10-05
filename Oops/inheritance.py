"""
Single Inheritance:
single inheritance  in object oriented programming refers to concepts class inherting
attrinbutes and methods from single parent class.we can achive single inheritance
by creating a new class it inheriting single base class.
"""

class A:
    pass
class B(A):
    pass

print("Example for single inheritance")

class Animal:

    def __init__(self,name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return f"{self.name} is barking"


class Cat(Animal):

    def speak(self):
        return f"{self.name} it says meow"


dog = Dog('street dog')
cat = Cat('sweety')
print(dog.speak())
print(cat.speak())

class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius =  radius

    def area(self):
        return 3.14 * self.radius ** 2


c1 = Circle('circle',15)
area = c1.area()
print(area)


print("\n")
class Vehicle:

    def __init__(self,company,model):
        self.company = company
        self.model = model

    def milage(self):
        pass


class Car(Vehicle):

    def __init__(self,company,model ,color,engine_model):
        super(Car, self).__init__(company,model)
        self.colour = color
        self.engine_model = engine_model

    def milage(self):
        pass


print("Examples for multiple inheritance")


class Father:

    def __init__(self,FatherName):
        self.father = FatherName




class Mother:

    def __init__(self,MotherName):
        self.mother = MotherName


class Son(Father,Mother):

    def __init__(self,FatherName,MotherName,SonName):
        Father.__init__(self,FatherName)
        Mother.__init__(self,MotherName)
        self.son = SonName


    def family_info(self):
        return f"{self.father} and {self.mother} and {self.son}"



s1 = Son('Srinivas Rao','Laxmi','Suvarna')
info = s1.family_info()
print(info)


"""
Method resolution order:
Method resolution order is order in which programming language determine wich method or attribute to invoke
when there are in multiple inheritance.

How Method resolution order works:

"""

"""
Multilevel inheritance:
In python multilevel inheritance is type of inheritance in wich a derived class inherits from base class.
and another class inherites from derived class.this creates chain of inheritance in multiple level.
in each level of this inheritance adds new attributes and methods.

"""

class A:
    pass

class B(A):
    pass

class C(B):
    pass

print("Example for multilevel inheritance")

class Employee:

    def __init__(self,employee_id,employee_name):
        self.employee_id = employee_id
        self.Name = employee_name

    def dispaly_info(self):
        print("EmployeeId is: ",self.employee_id)
        print("Employee_name:",self.Name)

class Manager(Employee):

    def __init__(self,employee_id,employee_name,department):
        super().__init__(employee_id,employee_name)
        self.department = department

    def dispaly_info(self):
        super().dispaly_info()
        print("DepartName:",self.department)





class SeniorManager(Manager):

    def __init__(self,employee_id,employee_name,department,team_size):
        super().__init__(employee_id,employee_name,department)
        self.team_size = team_size

    def info(self):
        super().dispaly_info()
        print("Total team size:",self.team_size)


emp = Employee('46196090','Vinodkarnati')
emp.dispaly_info()

manager = Manager(46196089,'Vanivishwanath','Engineering')
manager.dispaly_info()


sm = SeniorManager('78596844','Prudvi raj','Networking',20)
sm.info()

print("\n")

class BankAccount:

    def __init__(self,ac_number,balance):
        self.account_number = ac_number
        self.balance = balance


    def validate_pin(self):
        self.pin = input("Enter Your pin here:")
        atm_pin = self.pin
        if len(atm_pin) == 4:
            print("Validated successfull")
        return self.balance

    def display_balance(self):
        print("Total_balance:",self.balance)

class SavingsAccount(BankAccount):

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount


    def available_balance(self):
        self.display_balance()
        print("Available Balance is:",self.balance)



obj = SavingsAccount('006901858950',75000)
obj.display_balance()
obj.withdraw(1500)
obj.display_balance()




"""
Hierarical inheritance:
hierarical inheritanc is one of the types of inheritance in object-oriented programming.
In hierarical inhearitance multiple subclasses inherits from single base class.it means
single base class served as super class for multple subclasses.each subclass inherits  attributes and
behaviour from parent class
"""

print("Examples for hierarical inheritance")
class Animal:

    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):

    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} is sys bow bow")

class Cat(Animal):

    def speak(self):
        print(f"{self.name} says meow...")


dog = Dog('Buddy','black')
cat = Cat('kitten')
dog.speak()
cat.speak()




