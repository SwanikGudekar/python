class Account:

    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass= acc_pass

    def resetPass(self):
        print(self.acc_pass)

acc1 = Account (12345,"abcde")

print(acc1.acc_no)
print(acc1.resetPass()) # show error because acc_pass is in private class 