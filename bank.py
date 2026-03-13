class InsufficientFundsError(Exception):
    def __init__(self):
        self.message = 'Insufficient balance !!!'
        super().__init__(self.message)

class InvalidTransactionError(Exception):
    def __init__(self, *args):
        self.message = 'Invalid account number !!!'
        super().__init__(self.message)

accounts = {}

class Account:
    def __init__(self,acc_no,balance,owner):
        self.acc_no = acc_no
        self.balance = balance
        self.owner = owner
        accounts[self.acc_no] = self

    def deposit(self , amount):
        self.balance += amount
        return self.balance

    def withdraw(self , amount):
        if amount > self.balance :
            raise InsufficientFundsError()
        self.balance -= amount
        return self.balance
        

    def transfer(self , reciever, amount):
            if amount > self.balance:
                raise InsufficientFundsError()
            elif reciever.acc_no not in accounts:
                raise InvalidTransactionError()

            self.balance -= amount
            reciever.balance += amount
            return f'''{self.owner} account balance : {self.balance} 
{reciever.owner} account balance : {reciever.balance}'''
    
    def totalMoney(self):
        total = 0
        for item in accounts:
            if accounts[item].owner == self.owner:
                total += accounts[item].balance
        return total

            
 

class SavingsAccount(Account):

    def __init__(self, acc_no, balance, owner , interest_rate , min_bal):
        super().__init__(acc_no, balance, owner)
        self.interest_rate = interest_rate
        self.min_bal = min_bal

class CheckingAccount(Account):
    def __init__(self, acc_no, balance, owner, overdraft_limit):
        super().__init__(acc_no, balance, owner)
        self.overdraft_limit = overdraft_limit

acc1 = Account(1 , 20000 , 'Devansh')
# acc1.deposit(5000)
# print(acc1.withdraw(50000))
acc2 = Account(2 , 15000, 'Sujal')
# print(acc2.transfer(acc2,10000))

acc3 = SavingsAccount(3, 25000, 'Devansh', 5, 10000)
acc4 = Account(4 , 10000, 'Sujal')
print(acc2.totalMoney())