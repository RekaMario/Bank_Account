class BankAccount:
    bank_name="raiffaisen"
    accounts = []
    def __init__(self, int_rate, balance, user): 
        self.accountHolder = user
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if (self.balance - amount) < 0 :
            print ("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return self
        else:
            self.balance -= amount
            return self

    def yield_interest(self):
        if self.balance  <= 0 :
            return self
        else :
            self.balance += (self.balance * self.int_rate)
            return self
            
    @classmethod
    def display_account_info(cls):
        for account in cls.accounts:
            print( "User :" + account.accountHolder )
            print("      Your balance is :" +  str(account.balance))

romario = BankAccount(0.3, 1200, "Romario Reka")
endi = BankAccount(0.3, 1200 , "Endi Mimini")

romario.deposit(200).deposit(300).withdraw(300).withdraw(200).withdraw(1200).yield_interest().display_account_info()
endi.deposit(300).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()