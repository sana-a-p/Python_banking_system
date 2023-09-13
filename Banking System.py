''' python project for a banking system which includes :
1.user login using username, password, account number
2.deposit money
3.withdraw money
4.checking bank balance'''

user_ls=["SANA","LORELAI","RORY","LUCAS","DANE"]
password={"SANA":"s@123abc","LORELAI":"lo@456def","RORY":"r@789ghi","LUCAS":"lu@101jkl","DANE":"d@102mno"}
account_no={"SANA":7895490453,"LORELAI":6743890348,"RORY":784309127,"LUCAS":7853409569,"DANE":1290459340}
balance={"SANA":75002,"LORELAI":35467,"RORY":23907,"LUCAS":50700,"DANE":13908}


print("******Welcome to IBIB BANK******")

print("Enter:")
print("1.Sign in\n2.Sign up")
ch1=int(input("Enter your choice:- "))
if ch1==1:
    name=input("Enter the username:- ")
    user_name=name.upper()
    pw=input("Enter the password:- ")
    accno=int(input("Enter the account number:- "))
    print("Hello", name)
    if user_name in user_ls:
        if password[user_name]==pw:
            if account_no[user_name]==accno:
                while True:
                    print("$$$$$$$$$$$$ MENU $$$$$$$$$$$$")
                    print("Enter:")
                    print("1.Deposit money\n2.Withdraw money\n3.Check bank balance\n4.Exit")
                    ch2=int(input("Enter your choice:- "))
                    if ch2==1:
                        dep_value=float(input("Enter the value to be deposited:- "))
                        if dep_value>0:
                            balance[user_name]+=dep_value
                            print("Your account balance is ",balance[user_name])
                        else:
                            print("Sorry!...please enter a valid deposit value")
                    elif ch2==2:
                        wd_value=float(input("Enter the value to be withdrawn:- "))
                        if wd_value<=balance[user_name]:
                            balance[user_name]-=wd_value
                            print("Your account balance is ", balance[user_name])
                        else:
                            print("Sorry!...you don't have enough bank balance")
                    elif ch2==3:
                        print("Your account balance is ", balance[user_name])
                    elif ch2==4:
                        print("Thank you for using IBIB BANK online service")
                        print("Exiting...")
                        print("Visit again")
                        print("************************")
                        break
                    else:
                        print("Sorry!...Invalid choice, please enter a valid choice..")

            else:
                print("Sorry!...Invalid account number, please enter a valid one..")
        else:
            print("Sorry!...Invalid password, please enter a valid one..")
    else:
        print("Sorry!...Invalid username, please enter a valid one..")
elif ch1==2:
    name = input("Enter the username:- ")
    user_name=name.capitalize()
    pw = input("Enter the password:- ")
    accno = int(input("Enter the account number:- "))
    if name.isalpha():
        user_name=name.upper()
        user_ls.append(user_name)
    else:
        print("Invalid username")
    password[user_name]=pw
    if 1000000000<=accno<=9999999999:
        account_no[user_name]= accno
    else:
        print("Invalid account number")
    print("You have successfully singned up ....")
else:
    print("Sorry!...Invalid choice, please enter a choice..")
    print("Thank you for using IBIB BANK online service")
    print("Exiting...")
    print("Visit again")
    print("*********************")