
from abc import ABCMeta,abstractmethod
from random import randint
class Account(metaclass = ABCMeta):
    @abstractmethod
    def createnewaccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0

class SavingAccount(Account):
    def __init__(self):
        self.savingaccounts ={}
    def createnewaccount(self,name,initialdep):
        self.accountNumber = randint(10000,99999)
        self.savingaccounts[self.accountNumber] = [name,initialdep]
        print("Account Creation is successul.your account number is",self.accountNumber)

    def authenticate(self,name,accountnumber):
        if accountnumber in self.savingaccounts.keys():
            if self.savingaccounts[accountnumber][0] == name:
                print("Authentication successful")
                self.accountNumber = accountnumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication faliure")
            return False

    def withdraw(self,withdrawlamt):
        if withdrawlamt > self.savingaccounts[self.accountNumber][1]:
            print("insufficient balance")
        else:
            self.savingaccounts[self.accountNumber][1] -= withdrawlamt
            print("withdrawl was succesfull")
            self.displayBalance()

    def deposit(self,depositamt):
        self.savingaccounts[self.accountNumber][1]  += depositamt
        print("depsit was succesful")
        self.displayBalance()

    def displayBalance(self):
        print("Avaialble Balnace",self.savingaccounts[self.accountNumber][1])


savings = SavingAccount()

while True:
    print("Enter 1 t o crete new acocunt")
    print("Enter 2 to access existing account")
    print("Enter 3 to exit")
    userchoice = int(input())
    if userchoice is 1:
        print("Enter your Name")
        name = input()
        print("Enter the intial deposit")
        deposit = int(input())
        savings.createnewaccount(name,deposit)
    if userchoice is 2:
        print("enter name ")
        name = input()
        print("Enter account number")
        accountnumber = int(input())
        status = savings.authenticate(name,accountnumber)
        if status is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to dpeosit")
                print("Enter 3 to diplay mbalance")
                print("Enter 4 to go bakc to previous account")
                userchoice = int(input())
                if userchoice is 1:
                    print("Enter withdraw amunt")
                    withdrawlamt = int(input())
                    savings.withdraw(withdrawlamt)
                elif userchoice is 2:
                    print("Enter depsit amoutn")
                    depositamt = int(input())
                    savings.deposit(depositamt)
                elif userchoice is 3:
                    savings.displayBalance()
                elif userchoice is 4:
                    break
    elif userchoice is 3:
        quit()
