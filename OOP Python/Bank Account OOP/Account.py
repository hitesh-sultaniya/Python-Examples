class MyAccount(object):

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath,"r") as balanceFile:
            self.balance = int(balanceFile.read())

    def withDrawMoney(self,amount):
        self.balance = self.balance - amount

    def depositMoney(self,amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath,"w") as balanceFile:
            balanceFile.write(str(self.balance))


class Checking(MyAccount):

        def __init__(self,filepath,charges):
            self.charges = charges
            MyAccount.__init__(self,filepath)

        def transferAmount(self,amount):
            self.balance = self.balance - amount - self.charges



checking = Checking("balance.txt",100)
checking.transferAmount(200)
print(checking.balance)
checking.commit()
