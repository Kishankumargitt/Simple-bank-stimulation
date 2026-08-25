class Account:
    def __init__(self,id,holder_name,balance=0):
        self.holder_name=holder_name
        self._balance=balance
        self.id = id

    def Balance(self):
        print(f"Balance =: {self._balance}") 

    def deposit(self,amount):
        self._balance += amount
        print(f"Amount deposited {amount} ,balance is {self._balance}")

    def withdraw(self,amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Amount withdrawed {amount} , current balance is {self._balance}")
        else:
            print("insuffent balance")
    

class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.05 
        interest = self._balance * INTEREST_RATE 
        print(f"Interest calculated: {interest}")


     
class CurrentAccount(Account): 
    def withdraw(self,amount):
        OVER_DRAFT = 1000
        if self._balance+OVER_DRAFT >= amount:
            self._balance -= amount
            print(f"Amount withdrawed, current balance is {self._balance} ")
        else:
            print("insuffent balance")


class bank:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
        self.accounts = accounts={}
    def create_account(self,id,holder_name,type):
        if type == "savings":
            new_account = SavingsAccount(id,holder_name) 
        elif type == "current":
           new_account = CurrentAccount(id,holder_name)
        else:
            print("Invalid account type")
        self.accounts[id] = new_account
        print(f"Account created successfully for {holder_name} with id {id}")
        return new_account
 
    def get_account(self,id):
        if id not in self.accounts:
           print("Account not found")
        else:
          account = self.accounts[id]
          print(f"Account found for {account.holder_name} with id {id}")


kkb = bank("Canara bank","shankaranarayana")

s1 = kkb.create_account("1","kishan kumar","savings")
c1 = kkb.create_account("2","suresh kumar","current")

s1.deposit(1000)
c1.deposit(5000)

s1.Balance()
c1.Balance()

s1.withdraw(500)
c1.withdraw(600)

s1.calculate_interest()      