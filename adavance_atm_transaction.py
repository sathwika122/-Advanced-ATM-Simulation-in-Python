correct_pin='123'
balance=10000
attempts=0
max_attempts=3
transaction=[]
while True:
    entered_pin=input("enter your pin: ")
    if entered_pin==correct_pin:
        print("PIN verification is successfully done!")
        break
    else:
        attempts=attempts+1
        print("Incorrect Pin,attempts left:",(max_attempts-attempts))
        if attempts>=max_attempts:
            print("your ATM card is bocked due to limit is exceed")
            exit()
while True:
    print("....main menu....")
    print("press 1 for balance checking")
    print("press 2 for deposit")
    print("press 3 for withdrawn")
    print("press 4 for transactions(last 4 transaction")
    print("press 5 for exit")
    choice=input("enter your choice: ").strip()
    if choice == "1":
        print("your account balance is: ",balance)
    elif choice == "2":
        deposit_amount=int(input("enter the you want to deposite: "))
        if deposit_amount>0:
            balance=balance+deposit_amount
            transaction.append(f"deposited is {deposit_amount}")
            if len(transaction)>5:
                transaction.pop(0)
            print("deposit is successfull new balance is:",balance)
        else:
            print("invalid amount")
    elif choice=="3":
        withdraw_amount=int(input("Enter the you want to withdraw: "))
        if 0< withdraw_amount<=balance:
            balance=balance-withdraw_amount
            transaction.append(f"withdrawn: {withdraw_amount}")
            if len(transaction)>5:
                transaction.pop(0)
            print("withdraw is successfull,New balance is: ",balance)
        else:
            print("Insufficient balance or invalid amount")
    elif choice=="4":
        print("currrent transactions are: ")
        if len(transaction)==0:
            print("No transaction is done upto now")
        else:
            for t in transaction:
                print(t)
    elif choice=="5":
        print("Thankyou for visiting...")
        break
    else:
        print("invalid options")
                               

    


