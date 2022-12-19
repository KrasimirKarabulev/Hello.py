from errors import InvalidAccountType, UnsufficientBalance

class Account:
    ACC_TYPES = ("CURRENT", "SAVING", "CREDIT")

    def __init__(self, iban, currency, type) -> None:
        if type not in Account.ACC_TYPES:
            raise InvalidAccountType()
        
        self.iban = iban
        self.currency = currency
        self.type = type

    def print_acc(self):
        print(f"Iban: {self.iban}, Currency: {float(self.currency)}, Type: {self.type}")
        
    def plus(self, amount):
        self.currency=float(self.currency)+float(amount)
        print(f"New currency = {self.currency}")

    def minus(self, amount):
        if float(self.currency)-float(amount)<0:
            raise UnsufficientBalance()
        else:
            self.currency=float(self.currency)-float(amount)
            print(f"New currency = {self.currency}")