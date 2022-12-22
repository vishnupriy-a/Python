class BankAccount:
	account_no = 0
	name = ""
	account_type = ""
	balance = 0.0
	
	def __init__(self):
		self.account_no = int(input("Enter account number: "))
		self.name = input("Enter name: ")
		self.account_type = input("Enter account type: ")
		self.balance = float(input("Enter balance: "))
	def display(self):
		print("Account No:", self.account_no)
		print("Name:", self.name)
		print("Account Type:", self.account_type)
		print("Balance:", self.balance)

	def deposit(self):
		self.balance += float(input("Enter amount to depost: "))
		print("New balance is: ", self.balance)
	def withdraw(self):
		withdraw_amount = float(input("Enter amount to withdraw: "))
		if withdraw_amount > self.balance:
			print("Balance not sufficient\n")
			return
		self.balance -= withdraw_amount
		print("New balance is: ", self.balance)

obj1 = BankAccount()
obj1.display()
obj1.deposit()
obj1.withdraw()
obj1.withdraw()
