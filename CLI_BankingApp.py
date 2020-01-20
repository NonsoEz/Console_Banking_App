import json

class BankApp:

    def __init__(self):
        self.users = {}
        self.account_balance = 0.0


    def create_user(self):
        email = input("Enter email: ").lower()
        if ("@" in email) and ("." in email):
            if email in self.users.keys():
                print("User already exists ")
            else:
                try:
                    pin =  int(input("Create 4-digit pin: "))
                except ValueError:
                    print("Use only numbers")
                    return self.create_user()
                # initialize the balance to $0.0
                self.account_balance = 0.0
                self.users[email] = {"pin": pin, "account_balance": self.account_balance}
                print(f"Account created successfully! Your account balance is: {self.account_balance}")
                print(self.users)
                with open('usersdata.json', 'a+') as userdetail:
                    json.dump(self.users, userdetail, indent=4)
        else:
            print("Email is not valid, Please try again")
            self.create_user()

    
    def transaction(self):
        # ask the user to enter pin
        #email = input("Enter email: ")
        login_prompt = int(input("Enter 4-digit pin to proceed: "))
        # check if pin is a match
        with open("usersdata.json") as userdetail:
            data = json.load(userdetail)
        if login_prompt not in data:
            print("Invalid pin")
            return self.transaction()
        else:
            transaction_prompt = (int(input("Press 1: Check Balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n>> " )))
            # display actions to perform
            if transaction_prompt == 1:
                return self.check_balance(email)
            elif transaction_prompt == 2:
                return self.deposit(email)
            elif transaction_prompt == 3:
                return self.withdraw(email)
            elif transaction_prompt == 4:
                return self.transfer(email)
            else:
                print("Incorrect entry")
                self.transaction()

    def check_balance(self, email):
        account_balance = self.users[email]["account_balance"]
        print(f"Your balance is: N{account_balance}")
        return self.transaction()


    def deposit(self, email):
        global account_balance
        deposit_amount = int(input("Enter amount to deposit: "))
        account_balance += deposit_amount
        print(f"Transaction successful! \nYour new account balance is N{account_balance}")
        print("Thanks for banking with us!")
        return self.transaction()


    def withdraw(self, email):
        global account_balance
        withdraw_amount = int(input("Enter amount for withdrawal: "))
        if withdraw_amount > account_balance or account_balance <= 1000.0:
            print("Insufficient funds")
            return self.deposit()
        else:
            account_balance -= withdraw_amount
            print(f"You have successfully withdrawn {withdraw_amount} \nYour balance is {account_balance}")


    def transfer(self, email):
        receipient = input("Enter receipient's email: ")
        with open('usersdata.json') as userdetail:
            data = json.load(userdetail)
        if receipient not in data:
            print("Invalid beneficiary account")
            self.transfer(email)
        transfer_amount = float(input("Enter amount for transfer: "))
        while True:
            try:
                valid_amount = float(transfer_amount)
                if valid_amount > 0.0:
                    break
                else:
                    print("Invalid amount, please enter figures only")
                    transfer_amount = input("Please enter the amount to transfer")
            except ValueError:
                print("Invalid amount, please enter figures only")
                transfer_amount = float(input("Enter amount to be transferred: "))
        current_balance = self.users[email]["account_balance"]
        if transfer_amount > account_balance or account_balance <= 1000.00:
            print("Insufficient funds")
            return self.deposit()
        elif receipient not in users:
            print("Invalid User")
            #return receipient = input("Enter receipient's email: ")
        else:
            pass





BankingApp1 = BankApp()

print(BankingApp1)

#First prompt to user 
first_prompt = int(input("Press 1: Create Account \nPress 2: Transaction \nPress 3: To quit  \n>> " ))
while True:
    if first_prompt == 1 or first_prompt == 2 or first_prompt == 3:
        break
    else:
        print("Invalid selection")
        first_prompt = int(input("Press 1: Create Account \nPress 2: Transaction \nPress 3: To quit\n>> "))
    if first_prompt == 1:
        BankingApp1.create_user()
    elif first_prompt == 2:
        BankingApp1.transaction()
    elif first_prompt == 3:
        print("Session Ended")
        quit()