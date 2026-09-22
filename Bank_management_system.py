

accounts = []
class bank:
        def __init__(self,acc_no, name, pin, balance, acc_type):
            self.acc_no = acc_no
            self.name = name
            self.pin = pin
            self.balance = balance
            self.acc_type = acc_type

while True:
    print('''===============================
      WELCOME TO MY-BANK
==============================
1. create account
2. log in
3. exit''')
    user_choice = int(input("\n enter your choice :"))

#if user wants to create account
    if user_choice == 1:
        acc_no = len(accounts) + 1
        name = input("\n enter your name : ")
        while True:
            pin = (input("\n set your 4-digit pin : "))
            if len(pin) == 4 and pin.isdigit():
                 break
            else:
                print("\n pin should be of only 4 numbers") 
                 

        while True:
            acc_type = input("\n press 'S' for savings account or press 'C' current account : " )
            if acc_type.lower() == "s" or acc_type.lower() == "c" :
                break
            else:
                 print("\n please enter wether 's' or 'c' and not any other word ")

#used error handling concept
        while True:
            try:
                balance = int(input("\n enter your initial deposit (minimum 1000 rupees is required) : "))

                if balance >= 1000:
                    break
                elif balance < 0:
                    print("\n balance can't be negative")
                else:
                    print("\n sorry, amount more than 1000 is required in initial deposit")

            except ValueError:
                print("\n balance should be a number")
                    
        user = bank(acc_no, name, pin, balance, acc_type)
        accounts.append(user)

        print("\n account created succesfully!!")
        print("welcome to MY-BANK ", name)
        print(f"your account numer is {acc_no}")

    
    elif user_choice == 2:
        if len(accounts) == 0:
            print("\n no account exists, please create an account first")
            continue
        logout = False
        while True:

            entered_acc_no = int(input("enter your account number : "))
            entered_pin = (input("enter your pin : "))

            for account in accounts:
                if account.acc_no == entered_acc_no:
                    if account.pin == entered_pin:
                        print("\n login succesfully ")
                        while True:
                            print(f'''===============================
                                welcome to your account {account.name}
                            ===============================
                            1.check balance
                            2.deposit money 
                            3.withdraw money
                            4.view account details
                            5.Transfer money(you can only transfer money with persons whose account is in same bank)
                            6.change pin
                            7.delete account
                            8.logout
                            ''')

                            account_choice = int(input("enter your choice for service : "))

                            if account_choice == 1:
                                print(f"current balance = {account.balance}")
                            elif account_choice == 2:
                                while True:
                                    amount_add = int(input("enter the amount want to deposit : "))  
                                    if amount_add > 0:
                                        account.balance += amount_add        
                                        print(f'''amount added : {amount_add}
                                        new balance : {account.balance}''')
                                        break
                                    elif amount_add < 0:
                                        print("amount can' be negative")
                                    else:
                                        print("enter numbers only")    

                            elif account_choice == 3:
                                while True:
                                    amount_withdraw = int(input("enter the amount want to withdraw : "))   
                                    
                                    if amount_withdraw > account.balance:
                                        print("insufficient balance") 
                                    elif amount_withdraw <= 0:
                                        print("amount can't be negative")
                                    elif amount_withdraw <= account.balance:
                                        account.balance -= amount_withdraw        
                                        print(f"amount {amount_withdraw} withdrawned successfully")
                                        print(f"new balance is {account.balance}")
                                        break
                                    else:
                                        print("enter numbers only")   

                            elif account_choice == 4:
                                print(f'''account number : {account.acc_no}
                                name : {account.name}
                                account type : {account.acc_type}
                                balance : {account.balance}''') 

                            elif account_choice == 5:
                                receiver_acc_no = int(input("enter receivers account number : "))
                                found = False

                                for receiver_account in accounts:
                                    if receiver_acc_no == receiver_account.acc_no:
                                        found = True

                                        if receiver_account.acc_no == account.acc_no:
                                            print("you cannot transfer money to yourself")
                                        else:
                                            money_trans = int(input("enter the amount you want to transfer : "))
                                            if money_trans <= 0:
                                                print("pleaxe add a positive value")
                                            elif money_trans > account.balance:
                                                print("sorry, not enough balance")  
                                            else:
                                                receiver_account.balance += money_trans
                                                account.balance -= money_trans
                                                print("transaction succesfull")

                                        break
                                            

                                if not found:
                                    print("user not found")
                            
                                    
                            elif account_choice == 6:
                                your_acc_no = int(input("enter your account number :"))
                                found = False
                                for account in accounts:
                                    if your_acc_no == account.acc_no:
                                        found = True
                                        current_pin = input("enter your current pin :")
                                        if current_pin == account.pin:
                                            while True:
                                                new_pin = input("enter your new 4 digit pin : ")
                                                if len(new_pin) != 4 or not new_pin.isdigit():
                                                    print("PIN SHOULD BE OF 4 DIGIT's ONLY")

                                                else:
                                                    account.pin = new_pin
                                                    print("PIN updated succesfully")
                                                    break
                                            break
                                        else:
                                            print('wrong pin, please enter the correct pin')
                                            break
                                if not found:
                                    print("account doesn't exist")
                                            
                            elif account_choice == 7:
                                your_acc_no = int(input("enter your account number :"))
                                found = False
                                for account in accounts:
                                    if your_acc_no == account.acc_no:
                                        found = True
                                        current_pin = input("enter your current pin :")
                                        if current_pin == account.pin:
                                            
                                            consent = input("are you sure to delete the account (yes/no) : ")
                                            if consent.lower() == "no":
                                                break
                                            elif consent.lower() == "yes":
                                                accounts.remove(account)
                                                print("account removed succesfully")
                                                break
                                            else:
                                                print("enter wether yes or no")
                                        
                                        else:
                                            print('wrong pin, please enter the correct pin')
                                            break
                                if not found:
                                    print("account doesn't exist")

                            elif account_choice == 8:
                                logout = True
                                break
                                       
            if logout:
                break
                           

                            


                            
                    


                            

        
        
