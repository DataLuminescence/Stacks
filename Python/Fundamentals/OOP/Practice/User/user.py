class User:		# here's what we have so far
    bank_name = "First National Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
felix = User("Felix the Cat", "felix@fleamail.com")

guido.make_deposit(200)
guido.make_deposit(450)
guido.make_deposit(350)
guido.make_withdrawal(500) 
guido.display_user_balance() #Should return 500

monty.make_deposit(300)
monty.make_deposit(200)
monty.make_withdrawal(100)
monty.make_withdrawal(200)
monty.display_user_balance() #Should return 200

felix.make_deposit(1000)
felix.make_withdrawal(250)
felix.make_withdrawal(150)
felix.make_withdrawal(100)
felix.display_user_balance() #Should return 500

guido.transfer_money(felix, 200) #Should return 700
