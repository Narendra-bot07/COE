amount = 0


def validation():
    count=3

    while(count>0):
        pin = int(input('Enter your PIN number: '))
        if pin == 1234:
            return True
        else:
            print("You entered wrong pin")
            count=count-1
            print(f"you have {count} chances left")



print('Welcome to ABC Bank')
if validation():
    while True:
        print("1.Deposit\n2.Withdraw\n3.Bal Enquiry \n4.Exit  \n choose your choice")
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                dmount = int(input("Enter amount to deposit: "))
                amount = amount + dmount
            case 2:
                wmount = int(input("Enter amount to withdraw: "))
                amount = amount - wmount
            case 3:
                print("Available amount ", amount)
            case 4:
                exit()
            case _:
                print("Invalid choice")

else:
    print("Your account blocked")
