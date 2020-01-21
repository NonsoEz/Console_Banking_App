import json

class BankApp:

    def __init__(self):
        self.users=[]

        #self.prompt()
            
        with open('usersdata.json') as json_file :
            self.users = json.load(json_file)

    """def prompt(self):
        print("Welcome to Virtual Gardens Group Bank")
        print("Press 1: Create Account\nPress 2: Transaction\nPress 3: To Quit\n")
        try:
            welcome_prompt = int(input(">> "))
        except ValueError:
            print("\nPlease choose 1, 2 or 3\n")
            self.prompt()
        if (welcome_prompt == 1):
            self.create_user()
        elif (welcome_prompt == 2):
            self.transaction()
        elif (welcome_prompt == 3):
            quit()
        else:
            print("\nPlease choose 1, 2 or 3\n")
            self.prompt()"""


    def create_user(self):
        email = input("Enter email: ").lower()
        if ("@" in email) and ("." in email):
            #check if user exists
            if email in self.users:
                print("User already exists ")
                return self.create_user()
            else:
                try:
                    """ 
                    pin variable is retrieved as a string object to enable the len() function to 
                    check number of characters. Function int(pin) enables ValueError to check for
                    values that are not integers but does not change the datatype of pin.
                    """
                    pin =  str(input("Create 4-digit pin: "))
                    int(pin)
                except ValueError:
                    print("Use only numbers")
                    return self.create_user()
                #check for length of pin
                if len(pin) != 4:
                    print("Pin must be 4 digits only.")
                    return self.create_user()
                user = {"email": email, "pin": pin, "balance": 0.0}

                self.users.append(user)
                #figure out why data is not persistent?
                with open('usersdata.json', 'w') as userdetail:
                    json.dump(self.users, userdetail, indent=4)
                
                bal = user["balance"]
                print(f"Account created successfully! Your account balance is: {bal}")
                print(self.users)
                #self.prompt()
        else:
            print("Email is not valid, Please try again")
            self.create_user()

        
    def transaction(self):
        pass
        '''with open('usersdata.json') as json_file :
            data = json.load(json_file)
        print("Please login")
        # ask the user to enter email
        email = input("Enter email: ")
        if email not in data.keys():
            print("User does not exist.\nKindly re-enter correct details or create an account")
            self.prompt()
        else:
            # check if pin is a match
            pin = int(input("Enter pin: "))
            if pin in data.values():

        
        if login_pin not in data:
            print("Invalid pin")
            return self.transaction()
        else:
            transaction_prompt = (input("Press 1: Check Balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n>> " ))
            # display actions to perform
            if transaction_prompt == 1:
                return self.check_balance()
            elif transaction_prompt == 2:
                return self.deposit()
            elif transaction_prompt == 3:
                return self.withdraw()
            elif transaction_prompt == 4:
                return self.transfer()
            else:
                print("Incorrect entry")
                self.transaction()
        '''

#creating an object of class
s = BankApp()
    
#calling functions with that class object
"""s.prompt()"""
s.create_user()




"""def transaction(self):
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
            transaction_prompt = (input("Press 1: Check Balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n>> " )):
            # display actions to perform
            if transaction_prompt == 1:
                return self.check_balance()
            elif transaction_prompt == 2:
                return self.deposit()
            elif transaction_prompt == 3:
                return self.withdraw()
            elif transaction_prompt == 4:
                return self.transfer()
            else:
                print("Incorrect entry")
                self.transaction()
    
    def transaction(self): 
        #ask the user to enter pin
        email = input("Enter email: ")
        login_prompt = int(input("Enter 4-digit pin to proceed: "))
        #check if pin is a match
        with open("usersdata.json") as userdetail:
            data = json.load(userdetail)
        if login_prompt not in data:
            print("Invalid pin")
            return self.transaction()
        elif transaction_prompt = (int(input("Press 1: Check Balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n>> " ))):
            #display actions to perform
            if transaction_prompt == 1:
                return check_balance()
            elif transaction_prompt == 2:
                return deposit()
            elif transaction_prompt == 3:
                return withdraw()
            elif transaction_prompt == 4:
                return transfer()
            else:
                print("Incorrect entry")
                return transaction()

    def check_balance(self):
        print(f"Your balance is: N{self.account_balance}")
        return self.transaction()


    def deposit(self):
        global account_balance
        deposit_amount = float(input("Enter amount to deposit: "))
        account_balance += deposit_amount
        print(f"Transaction successful! \nYour new account balance is N{account_balance}")
        print("Thanks for banking with us!")
        return self.transaction()


    def withdraw(self):
        global account_balance
        withdraw_amount = int(input("Enter amount for withdrawal: "))
        if withdraw_amount > account_balance or account_balance <= 1000.0:
            print("Insufficient funds")
            return self.deposit()
        else:
            account_balance -= withdraw_amount
            print(f"You have successfully withdrawn {withdraw_amount} \nYour balance is {account_balance}")


    def transfer(self):
        global account_balance
        receipient = input("Enter receipient's email: ")
        transfer_amount = int(input("Enter amount for transfer: "))
        if transfer_amount > account_balance or account_balance <= 1000.00:
            print("Insufficient funds")
            return self.deposit()
        elif receipient not in users:
            print("Invalid User")
            #return receipient = input("Enter receipient's email: ")
        else:
            pass"""





