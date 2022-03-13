from optparse import check_builtin


class BankAccount:
    accounts = []
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate #Attribute that each new bank instance will have
        self.balance = balance #Attribute that each new bank instance will have
        BankAccount.accounts.append(self) #Creates a record in accounts list of each new bank account created
    
    def deposit(self, amount):
        #Points to itself because only account have a balance. We need user to point to account, then balance
        self.balance += amount  
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        if(self.balance < 0):
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            
        return self

    def display_account_info(self):
        print(f"{self.balance}")
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance*self.interest_rate
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info() 

class User:
    def __init__(self, name):
        self.name = name
        self.account = {"checking" : BankAccount(interest_rate=.02, balance=1000),
                        "savings" : BankAccount(interest_rate=.02, balance=800)
        }

    def make_deposit(self, amount ,account):
        self.account[account].deposit(amount) #Update

    def make_withdrawal(self, amount):
        self.account["checking"].withdrawal(amount)

    def display_user_balance(self): # pass info update
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, user, amount):
        self.account["checking"].withdrawal(amount)
        user.account["checking"].withdrawal(amount)
        self.account["checking"].display_account_info()
        user.account["checking"].display_account_info()
        return self

guido = User("Guido")
felix = User("Felix")

guido.account['checking'].deposit(100)
guido.account['savings'].deposit(100)

felix.account['checking'].deposit(50)
felix.account['savings'].deposit(50)

guido.transfer_money(felix, 200)

guido.display_user_balance()
felix.display_user_balance()