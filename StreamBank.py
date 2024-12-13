import streamlit as st
def validate():
    count = 3
    pin = st.text_input('Enter your pin', type='password', key='0')
    if st.button('Submit', key='3'):
        if pin == "1234":
            return True
        else:
                st.error("You entered wrong pin")
                count -= 1
                st.error(f"You have {count} chances left")
                if count == 0:
                    st.error("Your account is blocked due to too many wrong attempts.")
                    return False
    return False


def denomination(withdrawl):
    _500, _200, _100 = 0, 0, 0
    while withdrawl > 0:
        if withdrawl // 500 >= 1:
            _500 += 1
            withdrawl -= 500
        elif withdrawl // 200 >= 1:
            _200 += 1
            withdrawl -= 200
        else:
            _100 += 1
            withdrawl -= 100
    st.write("Denominations:-")
    st.write(f"500 x {_500} = ", 500 * _500)
    st.write(f"200 x {_200} = ", 200 * _200)
    st.write(f"100 x {_100} = ", 100 * _100)


class Bank:
    amount = 1000
    maxtransaction = 3

    def deposit(self):
        self.damount = st.number_input('Enter deposit amount', min_value=100, max_value=50000, step=100, key='1')
        if st.button('Deposit', key='4'):
            if self.damount < 100:
                st.error("Sorry, you can't deposit less than 100")
            elif self.damount > 50000:
                st.error("Sorry, you can't deposit more than 50000")
            elif self.damount % 100 != 0:
                st.error("Deposit amount should be multiples of 100")
            else:
                self.amount += self.damount
                st.success(f"Successfully deposited {self.damount}")
                self.display()

    def display(self):
        st.success(f"Available amount {self.amount}")

    def withdraw(self):
        if self.maxtransaction == 0:
            st.error("You cannot make transactions. You've reached the maximum limit for today (3).")
            return

        self.wamount = st.number_input('Enter withdraw amount', min_value=100, max_value=20000, step=100, key='2')
        if st.button('Withdraw', key='5'):
            if self.wamount > self.amount:
                st.error("You have insufficient balance")
                self.display()
            elif self.wamount < 100:
                st.error("Sorry, you can't withdraw less than 100")
            elif self.wamount % 100 != 0:
                st.error("Withdrawal amount should be multiples of 100")
            elif self.amount - self.wamount < 500:
                st.error("You should maintain at least 500 in your account")
            else:
                self.amount -= self.wamount
                self.maxtransaction -= 1
                st.success(f"{self.wamount} debited from your account")
                denomination(self.wamount)
                self.display()
                st.success(f"You are left with {self.maxtransaction} transactions for today")

    def displayOption(self):
        if validate():
            option = st.selectbox(
                "Select your operation",
                ("Deposit", "Withdraw", "Display", "Exit"),
            )
            if option == "Deposit":
                self.deposit()
            elif option == "Withdraw":
                self.withdraw()
            elif option == "Display":
                self.display()
            elif option == "Exit":
                st.stop()
            else:
                st.error("Invalid choice")
        else:
            st.error("Your account is blocked due to too many wrong PIN attempts")

obj = Bank()
obj.displayOption()
