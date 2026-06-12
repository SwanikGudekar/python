# create a account class with two attribute : balance and acc no.
# create a method for debit,credit,printing balance

class Account:

    #constructor
    def __init__(self,balance,acc):
        self.balance = balance
        self.acc = acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("debit:",amount)

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("cretit:",amount)

    #print bank balance
    def balancePrint(self):
        self.balancePrint
        print("Acc balance:",self.balance) 

 

s1 =Account(8000,123456789)
print("acc no.:",s1.acc)
print("acc balanace:",s1.balance)
s1.debit(1000)
s1.credit(500)
s1.balancePrint()
