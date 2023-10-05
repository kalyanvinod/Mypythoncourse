class BankAccount:

    def  __init__(self,account_number,balance):
        #Protected members
        self._account_number = account_number
        self._balance = balance

    def _validate_transaction(self,amount):
        return amount <= self._balance

    def _validate_deposit_amount(self,amount):
        return amount >=0

    def withdraw(self,amount):
        if self._validate_transaction(amount):
            self._balance -= amount
            print(f"Withdraw amount is : {amount},and available balance is :{self._balance}")

        else:
            print("Insufficent founds")

    def deposit(self,amount):
        if self._validate_deposit_amount(amount):
            self._balance +=amount
            print(f"Your Total balance is: {self._balance}")

        else:
            print("Failed Transaction")


sbi = BankAccount('00691585950',45000)
sbi.withdraw(10000)
sbi.deposit(2000)
sbi.withdraw(7000)
sbi.deposit(2500)
