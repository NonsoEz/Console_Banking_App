import json, os

class BankApp:

    def __init__(self):
        self.users=[]

        self.prompt()
            
        with open('usersdata.json', 'r') as json_file:
            self.users = json.load(json_file)

        #print(self.users)
        
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
        #Get current directory
        currentDirectory = os.getcwd()
        #store file name in a variable
        file_name = r'\\usersdata.json'
        #full path of json file
        total_path = currentDirectory + file_name
        #check if json file exists
        if os.path.isfile(total_path) and os.access(total_path, os.R_OK):
            print("File exists")
            with open('usersdata.json', 'r') as json_file:
                self.users = json.load(json_file)
            email = input("Enter email: ").lower()
            if ("@" in email) and ("." in email):
                #check if user exists
                if email in ([sub['email'] for sub in self.users]):
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
                    else:
                        pass
                    user = {"email": email, "pin": pin, "balance": 0.0}

                    print(self.users)
                    self.users.append(user)
                    with open('usersdata.json', 'w') as userdetail:
                        json.dump(self.users, userdetail, indent=4)

                    # get new user balance
                    bal = user["balance"]
                    print(f"Account created successfully! Your account balance is: ₦{bal}")
                    self.prompt()
            else:
                print("Email is not valid, Please try again")
                self.create_user()
        else:
            pass

            
    def transaction(self):
        #opens file for reading
        with open('usersdata.json', 'r') as json_file:
            data = json.load(json_file)
        print("Please login\n")
        # ask the user to enter email
        login_email = input("Enter email: ")
        login_pin = input("Enter pin: ")
        for i in data:
            if login_email == i["email"]:
                if login_pin == i["pin"]:
                    print("\nLogin successful!\nPlease proceed to select transaction\n")
                    transaction_prompt = int(input("Press 1: Check Balance \nPress 2: Deposit \nPress 3: Withdraw \nPress 4: Transfer \n>> " ))
                    # display actions to perform
                    if transaction_prompt == 1:
                        self.check_balance(login_email)
                    elif transaction_prompt == 2:
                        return self.deposit(login_email)
                    elif transaction_prompt == 3:
                        return self.withdraw(login_email)
                    elif transaction_prompt == 4:
                        return self.transfer(login_email)
                    else:
                        print("\nInvalid entry. Please try again\n")
                        self.transaction()
                else:
                    print("\nEmail or pin is incorrect. Try again.")
                    self.prompt()
                

    def check_balance(self, login_email):
        #opens file for reading
        with open('usersdata.json', 'r') as json_file:
            data = json.load(json_file)
        for i in data:
            if login_email == i["email"]:
                account_balance = i["balance"]
                print(f"Your balance is ₦{account_balance}\n")
                return self.transaction()
            else:
                pass


    def deposit(self, login_email):
        #opens file for reading and writing
        with open('usersdata.json', 'r') as json_file:
            data = json.load(json_file)
        #get deposit amount
        deposit_amount = float(input("Enter amount to deposit: "))
        for i in data:
            if login_email == i["email"]:
                i["balance"] += deposit_amount
                new_balance = i["balance"]
                with open('usersdata.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
        print(f"\nTransaction successful! \nYour new account balance is ₦{new_balance}")
        print("\nThanks for banking with us!\n")
        return self.transaction()


    def withdraw(self, login_email):
        #opens file for reading and writing
        with open('usersdata.json', 'r') as json_file:
            data = json.load(json_file)
        #get amount for withdrawal
        withdraw_amount = float(input("Enter amount for withdrawal: "))
        for i in data:
            if login_email == i["email"]:
                balance = i["balance"]
                if withdraw_amount > balance or balance <= 1000.0:
                    print("Insufficient funds\n Please deposit required amount\n")
                    return self.deposit(login_email)
                else:
                    i["balance"] -= withdraw_amount
                    new_balance = i["balance"]
                    with open('usersdata.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    print(f"\nYou have successfully withdrawn ₦{withdraw_amount} \nYour balance is ₦{new_balance}\n")
                    print("\nThanks for banking with us!\n")
                    self.prompt()

    
    def transfer(self, login_email):
        #opens file for reading and writing
        with open('usersdata.json', 'r') as json_file:
            data = json.load(json_file)
        beneficiary = input("Enter receipient's email: ")
        # loop through list of dictionaries to check if beneficiary mail exists in the system

        for i in data:
            if login_email == i["email"]:
                #sender's balance
                sender_balance = i["balance"]
    
                if beneficiary in ([sub["email"] for sub in data]):
                    transfer_amount = float(input("Enter amount to transfer: "))
                    if transfer_amount > account_balance or account_balance <= 1000.00:
                        print("Insufficient funds")
                        self.deposit(login_email)
                        #beneficiary's balance
                    else:
                        beneficiary_accountbalance = i["balance"]
                        account_balance -= transfer_amount
                        beneficiary_accountbalance += transfer_amount
                        print(f"Beneficiary's Account Balance: {beneficiary_accountbalance}")
                        print(f"User account balance {account_balance}")
                        #print("Transfer Successful!\nThank you for banking with us\n")
                        
                        with open('usersdata.json', 'w') as json_file:
                            json.dump(data, json_file, indent=4)
                        self.prompt()
                else:
                    print("Beneficiary doesn't exist, Please check email and try again!")
                    self.transfer(login_email)

            else:
                pass



#creating an object of class
s = BankApp()




