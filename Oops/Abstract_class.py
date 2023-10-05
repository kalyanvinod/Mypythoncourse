"""
in python abstract base class is class that cannot be instantiated itself but it serves as blueprint for another class
abstract base class is part of abc module.abc stands of abstract base class.

charecterstics of abstract base class:


"""
print("Exmaples for Abrastact class")

from abc import ABC ,abstractmethod
class Animal(ABC):

    def normal_method(self):
        print("This is Normal method")


    @abstractmethod
    def speak(self,name):
        pass

class Dog(Animal):

    def speak(self,name):
        self.name = name
        print(f"{self.name} is barking")

class Cat(Animal):

    def speak(self,name):
        self.name = name
        print(f'{self.name} is says meow')


dog = Dog()
cat = Cat()

dog.speak('Husky')
cat.speak("pussy cat")


print("\n")

class BankAccount(ABC):

    def __init__(self,account_number,balance):
        self.ac_number = account_number
        self.balance = balance

    @abstractmethod
    def withdraw(self,amount):
        pass



    @abstractmethod
    def deposit(self,amount):
        pass

    def get_balance(self):
        print(self.balance)


class SavingsAcount(BankAccount):

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Your available Balance is :",self.balance)
        else:
            print("Insufficent Balance")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Your Total Balance:", self.balance)
        else:
            print("Invalid amount:", amount)




my_account  = SavingsAcount('006901585950',75000)
my_account.withdraw(10000)
my_account.deposit(12000)
my_account.get_balance()

















