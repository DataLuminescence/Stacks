class User:		# here's what we have so far
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
felix = User("Felix the Cat", "felix@fleamail.com")

#Should return 500
guido.make_deposit(200).make_deposit(450).make_deposit(350).make_withdrawal(500).display_user_balance() 

#Should return 200
monty.make_deposit(300).make_deposit(200).make_withdrawal(100).make_withdrawal(200).display_user_balance() 

#Should return 500
felix.make_deposit(1000).make_withdrawal(250).make_withdrawal(150).make_withdrawal(100).display_user_balance() 

#Should return 700
guido.transfer_money(felix, 200) 
