class Bank:
    amount = 1000
    maxtransaction = 3

    def validate(self):
        count = 3
        while (count > 0):
            pin = int(input('Enter your PIN number: '))
            if pin == 1234:
                return True
            else:
                print("You entered wrong pin")
                count = count - 1
                print(f"you have {count} chances left")
    def denomination(self,withdrawl):
        _500, _200, _100 = 0, 0, 0
        while withdrawl>0:
            if withdrawl//500>=1:
                _500+=1
                withdrawl-=500
            elif withdrawl//200>=1:
                _200+=1
                withdrawl-=200
            else:
                _100 += 1
                withdrawl -= 100
        print("Denominations:-")
        print(f"500 x {_500} = ",500*_500)
        print(f"200 x {_200} = ", 200*_200)
        print(f"100 x {_100} = ", 100*_100)
    def deposit(self):
        while True:
            self.damount = int(input("Enter amount to deposit: "))
            if self.damount<100:
                print("Sorry, you can't deposit less than 100")
            elif self.damount>50000:
                print("Sorry, you can't deposit more than 50000")
            elif self.damount%100!=0:
                print("Deposit amount should be multiples of 100")
            else:
                self.amount+=self.damount
                break
    def display(self):
        print("Available amount ",self.amount)
    def withdraw(self):
        if self.maxtransaction == 0:
            print("You cannot make transactions..you reached maximum limit for today i.e 3")
        while self.maxtransaction > 0:
            self.wamount = int(input("Enter amount to withdraw: "))
            if self.wamount > 20000:
                print("Sorry, you can't withdraw more than 20000 at a time")
            else:
                if self.wamount > self.amount:
                    print("You have insufficient balance")
                    self.display()
                elif self.wamount < 100:
                    print("Sorry, you can't withdraw less than 100")
                elif self.wamount % 100 != 0:
                    print("withdrawl amount should be multiples of 100")
                elif self.amount-self.wamount<500:
                    print("you should maintain atleast 500 in ur account")
                else:
                    self.amount-=self.wamount
                    self.maxtransaction-=1
                    print(f"{self.wamount} debited from your account")
                    self.denomination(self.wamount)
                    self.display()
                    print(f"You are left with {self.maxtransaction} transactions for today")
                    break
    def displayOption(self):
        if self.validate():
            while True:
                print("1.Deposit\n2.Withdraw\n3.Bal Enquiry \n4.Exit  \n choose your choice")
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:
                        self.deposit()
                    case 2:
                        self.withdraw()
                    case 3:
                        self.display()
                    case 4:
                        exit()
                    case _:
                        print("Invalid choice")
        else:
            print("Your account Blocked")
obj = Bank()
obj.displayOption()