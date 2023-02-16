class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Heloo!!! Welcome to Deposit & Withdrawal Machine")
	
	def deposit(self):
		amount = float(input("Enter amount to be deposited : "))
		self.balance += amount
		print("Amount deposited: ",amount)
	
	def withdraw(self):
		amount = float(input("Enter amount to be withdraw : "))
		if self.balance >= amount:
			self.balance -= amount
			print("You withdraw : ",amount)
		else:
			print("Insufficent Balance")
	
	def display(self):
		print("Not available balance = ",self.balance)

s=Bank_Account()
s.deposit()
s.withdraw()
s.display()
