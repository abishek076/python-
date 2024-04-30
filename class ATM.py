class Account:
    def __init__(self,name):
        self.name1=name
        if self.name1=="rahul":
            def rahul(self):
                self.accountnumber=12345678
                self.pin=1234
                self.balance=30000
        elif name1=="kiran":
            def kiran(self):
                self.accountnumber = 1234567
                self.pin = 123
                self.balance = 300000


class ATM(Account):
    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited")
    def withdraw(self,amount):
        if self.balance>10000:
            self.balance-=amount
            print("Amount withdrew")
        else:
            print("Insufficient balance",self.balance)
    def ministatement(self):
        print("Account Number:",self.accountnumber)
        print("Your Balance:",self.balance)
    def checkbalance(self):
        print("Your Balance:", self.balance)
        print("Maximum withdraw:",self.balance-10000)


atm=ATM()
name=input("Enter your name:")
account=Account(name)
print("Hello Customer",account.accountnumber)
pin_number=int(input("Enter the pin number:"))

if pin_number==account.pin:
    print("choose number based on below choices")
    print("1.Deposit\n2.Withdraw\n3.Mini Statement\n4.Check balance")
    choice=int(input("Enter the choice:"))
    if choice==1:
        amount=int(input("Enter the deposit amount:"))
        atm.deposit(amount)
    elif choice==2:
        amount = int(input("Enter the withdraw amount:"))
        atm.withdraw(amount)
    elif choice==3:
        atm.ministatement()
    elif choice==4:
        atm.checkbalance()
else:
    print("pin_number is wrong, Try Again")