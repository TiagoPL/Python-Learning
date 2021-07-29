import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print(f'Account created for {self.name}')

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdraw(self, amount):
        if amount < 0:
            print('The amount must be greater than "0.00"')
        elif self.balance >= amount:
            self.balance = self.balance - amount
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), -amount))
        else:
            print(f"You don't have {amount} to withdraw")

    def show_balance(self):
        print(f'Balance is {self.balance}')

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'Deposited'
            else:
                tran_type = 'Withdrawn'
                amount = amount * -1
            print(f'{amount:6} {tran_type} on {date} (Local time was {date.astimezone()})')


tim = Account('Tim', 0)
tim.show_balance()
tim.deposit(1000)
tim.show_balance()
tim.withdraw(400)
tim.show_balance()
tim.show_transactions()
