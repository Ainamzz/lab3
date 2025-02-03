class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "Deposit:" + str(amount) + " New balance:" + str(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            return "Not enough money!"
        elif amount > 0:
            self.balance -= amount
            return "Withdrawn: " + str(amount) + " New balance: " + str(self.balance)

owner = input("Enter owner's name: ")

acc = Account(owner)
while True:
    action = input("Enter 'd' to deposit, 'w' to withdraw, or 'q' to quit: ")
    
    if action == 'd':
        amount = int(input("Enter deposit amount: "))
        print(acc.deposit(amount))
    
    elif action == 'w':
        amount = int(input("Enter withdrawal amount: "))
        print(acc.withdraw(amount))
    
    elif action == 'q':
        break
    
    else:
        print("Wrong input!")
