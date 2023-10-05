"""
Encapsulation:
Encapsulation is one of the  funcdamental conncept in oop .often it described  pillar of oop concepts
along with inheritance ,polymorphism.it is mechanism that allow us to bundle data and methods into a single unit
its called class.Encapsulation provide several benfits

Data hiding
controlled access
modularity
core reusablity
security


Data hiding:
Encapsulation is hidden the internal data of an object form the outside .This meanse internal data attributes
and method of an object can only be accessed or modified  well defined methods (getter and setter).how data is stored
and manipultaed its hidden from external code.

controlled access:
By using access modifies like private ,Protected,public encapsulation allow us to control to level of access
data members and methods in class

public members:
public members can access anywere outside from class
private member:
private members can access with in class
protected:
protected members can access with in the class and its subclass.

"""


print("Example for Private members")


class BankAccount:

    def __init__(self,account_number,balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

bankacount = BankAccount("006901858950",45000)
bankacount.deposit(8000)
balance = bankacount.get_balance()
print(balance)

bankacount.withdraw(25000)
outstanding_balance = bankacount.get_balance()
print(outstanding_balance)



class Myclass:

    def __init__(self):
        self.__private_attrtibute = 42

    def get_private_attribute(self):
        return self.__private_attrtibute

    def set_private_attribute(self,value):
        if value > 0:
            self.__private_attrtibute = value


obj = Myclass()
value = obj.get_private_attribute()
print(value)

obj.set_private_attribute(100)
value = obj.get_private_attribute()
print(value)



print("Another example private members")
class Myclass:

    def instance_method(self):
        print("This is instance method")


    def __private_method(self):
        print("This is private method")


    def public_method(self):
        result = self.__private_method()
        print("This is public method")
        return result



class NewClass(Myclass):

    def mymethod(self):
        self.public_method()
        print("This is method")

nc = NewClass()
nc.mymethod()



class StringManipulator:

    def __init__(self,text):
        self.__text = text

    def __remove_white_space(self):
        result = "_+_".join(self.__text.split())
        capital = self.__text.upper()
        return result,capital


    def result_method(self):
        method = self.__remove_white_space()
        return method


print("Examples for Protected variables")
"""
In object oriented programming Protected memebers are class memebers 
that have resticted access thay can be accessable with in the class and its subclass.

"""
class Animal:

    def __init__(self,name):
        self._name = name

    def show(self):
        print("This is protected Members :",self._name)

class Dog(Animal):

    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed


    def display_info(self):
        return f"{self._name} and {self.breed}"


dog = Dog("Buddy", "Golden Retriever")
result = dog.display_info()
print(result)








text = "   Hello,   World!   "
sm = StringManipulator(text)
mytext = sm.result_method()
print(mytext)



























