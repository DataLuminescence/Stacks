class BankaAccount:		# here's what we have so far
    bank_name = "First National Dojo"
    accounts = []
    def __init__(self, interestRate, balance):
        self.interestRate = interestRate
        self.balance = balance
        BankaAccount.accounts.append(self)
    
    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info() 
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance*self.interestRate
        return self



checking = BankaAccount(.01, 1000)
savings = BankaAccount(.05, 20000)

#Should return 500
checking.deposit(500).deposit(500).deposit(500).withdrawal(500).yield_interest().display_account_info()

#Should return 200
savings.deposit(500).deposit(500).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).yield_interest().display_account_info()


BankaAccount.print_accounts()

