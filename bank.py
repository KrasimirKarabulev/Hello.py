from random import randint
from errors import UserNotFound, UserAlreadyExists
from account import Account
from user import User

class Bank:
    def __init__(self) -> None:
        self.users = []

    def find_user(self, user_egn: str) -> User:
        for u in self.users:
            if u.egn == user_egn:
                return u
                
        return None

    def add_user(self, names, egn):
        found_user = self.find_user(egn)

        if type(found_user) == User:
            raise UserAlreadyExists()

        user = User(names, egn)
        self.users.append(user)

    def add_account(self, user_egn, currency, type):
        # user exists?
        found_user = self.find_user(user_egn)

        if found_user == None:
            raise UserNotFound()

        # generate iban
        iban = "BG9812"
        for i in range(0, 10):
            iban += str(randint(0, 9))

        # create account object
        account = Account(iban, currency, type)

        # call the user's add_account() method
        found_user.add_account(account)

    def list_all_accounts(self, egn):
        found_user = self.find_user(egn)
        found_user.list_accounts()

    def deposit(self, egn, iban, amount):
        found_user=self.find_user(egn)
        current_account=found_user.add_money_to_account(iban, amount)

    def withdrawal(self, egn, iban, amount):
        found_user=self.find_user(egn)
        current_account=found_user.withdraw_money_from_account(iban, amount)

    def print_ibans(self, egn):
        found_user=self.find_user(egn)
        found_user.print_ibans()