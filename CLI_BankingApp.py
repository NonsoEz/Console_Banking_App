import json

class BankApp:

    def __init__(self):
        self.users=[]

        self.prompt()
            
        with open('usersdata.json') as json_file:
            self.users = json.load(json_file)

    def prompt(self):
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
            self.prompt()


    def create_user(self):
        #opens file for reading
        with open('usersdata.json', 'r') as json_file:
            data = json.load(json_file)
        email = input("Enter email: ").lower()
        if ("@" in email) and ("." in email):
            #check if email exists in json file
            if email in ([sub['email'] for sub in data]):
                print("Email already exists, please use a unique email ")
                self.create_user()
            else:
                try:
                    """pin variable is retrieved as a string object to enable the len() function to 
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
                self.prompt()
        else:
            print("Email is not valid, Please try again")
            self.create_user()

        
    def transaction(self):
        #opens file for reading
        with open('usersdata.json') as json_file :
            data = json.load(json_file)
        print("Please login")
        # ask the user to enter email
        login_email = input("Enter email: ")
        # check if email exists in json file
        if login_email in ([sub['email'] for sub in data]):
            # check if pin is a match
            #might want to put an exception handler here
            login_pin = int(input("Enter pin: "))
            if login_pin in ([sub['pin'] for sub in data]):
                print("Login successful!\nPlease proceed to select transaction")
                transaction_prompt = (input("Press 1: Check Balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n>> " ))
                # display actions to perform
                if transaction_prompt == 1:
                    return self.check_balance(login_email)
                """elif transaction_prompt == 2:
                    return self.deposit(login_email, login_pin)
                elif transaction_prompt == 3:
                    return self.withdraw(login_email, login_pin)
                elif transaction_prompt == 4:
                    return self.transfer(login_email, login_pin)"""
            else:
                print("Invalid pin")
                self.transaction()
        else:
            print("Invalid email")
            self.prompt()


    def check_balance(self, login_email):
        #opens json file for reading
        with open('usersdata.json') as json_file :
            data = json.load(json_file)
        print(f"Your balance is: N{self.balance}")
        return self.transaction()


    """def deposit(self, login_email, login_pin):
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"Transaction successful! \nYour new account balance is N{balance}")
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





#creating an object of class
s = BankApp()
    
#calling functions with that class object
"""s.prompt()
s.create_user()"""
