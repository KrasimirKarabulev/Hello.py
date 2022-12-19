from errors import UserAlreadyOwnsAccount, InvalidAccountData, AccountNotFound
from account import Account

class User:
    def __init__(self, names, egn) -> None:
        self.names = names
        self.egn = egn
        self.accounts = []

    def get_print(self):
        return f"User({self.names}, {self.egn}, accounts: [{len(self.accounts)}])"

    def list_accounts(self):
        for acc in self.accounts:
           acc.print_acc()

    def add_account(self, account):
        if account in self.accounts:
            raise UserAlreadyOwnsAccount()
        else:
            self.accounts.append(account)

    def get_account(self, iban):
        for acc in self.accounts:
            if acc.iban==iban:
                return acc
            
        raise AccountNotFound()

    def print_ibans(self):
        for acc in self.accounts:
            print(f"Existing account's iban: {acc.iban}")

    def add_money_to_account(self, iban, amount):
        current_account=self.get_account(iban)
        current_account.plus(amount)
            
    def withdraw_money_from_account(self, iban, amount):
        current_account=self.get_account(iban)
        if current_account==None:
            raise AccountNotFound()
        else:
            current_account.minus(amount)
            