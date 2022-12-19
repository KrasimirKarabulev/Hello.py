from bank import Bank
from errors import InvalidUserData, InvalidMenuChoice, InvalidAccountData, InvalidAccountType, UserNotFound

class Menu:
    def print_menu(self):
        print("1. Register a new user")
        print("2. Create an account for an existing user")
        print("3. List all users")
        print("4. List all accounts for an existing user")
        print("5. Deposit money to a user account")
        print("6. Withdraw money from a user account")
        print("7. Exit")

    def run(self):
        bank = Bank()
        
        # infinite menu loop
        while True:  
            self.print_menu()
            choice = input("Choose an item from the menu: \n> ")

            try:
                if choice == "1":
                    names = input("Enter the user's names (alpha-only): ")
                    space_count=0
                    for i in names:
                        if i==" ":
                            space_count=space_count+1

                    if space_count!=1:
                        raise InvalidUserData("Names")

                    fname, lname = names.split(" ")
                    
                    if len(names) < 4 or not fname.isalpha() or not lname.isalpha():
                        raise InvalidUserData("Names")

                    egn = input("Enter the user's EGN number (len 10, digits-only): ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("EGN number")

                    bank.add_user(names, egn)

                elif choice == "2":
                    egn = input("Enter the existing user's EGN: ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("EGN number")
                    if bank.find_user(egn)!=None:
                        currency = input("Enter the currency of the account: ")
                        if not currency.isnumeric():
                            raise InvalidAccountData("Amount")
                        type = input("Enter the type of the newly created account(CURRENT, SAVING, CREDIT): ")
                        type=type.upper()
                        if type=="CURRENT" or type=="SAVING" or type=="CREDIT":
                            bank.add_account(egn, currency, type)
                        else:
                            raise InvalidAccountType()
                    else:
                        raise UserNotFound()

                elif choice == "3":
                    for u in bank.users:
                        print(u.get_print())

                elif choice == "4":
                    egn = input("Enter the existing user's EGN: ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("EGN number")
                    if bank.find_user(egn)!=None:
                        bank.list_all_accounts(egn)
                    else:
                        raise UserNotFound()

                elif choice == "5":
                    egn = input("Enter the existing user's EGN: ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("EGN number")
                    if bank.find_user(egn)!=None:
                        bank.print_ibans(egn)
                        iban=input("Enter an account's IBAN: ")
                        amount=input("Enter deposit: ")
                        try:
                            amount=float(amount)
                        except:
                            raise InvalidAccountData("Amount")
                        if amount>0:
                            bank.deposit(egn, iban, amount)
                        else:
                            raise InvalidAccountData("Negative amount")
                    else:
                        raise UserNotFound()

                elif choice == "6":
                    egn = input("Enter the existing user's EGN: ")
                    if len(egn) != 10 or not egn.isdigit():
                        raise InvalidUserData("EGN number")
                    if bank.find_user(egn)!=None:
                        bank.print_ibans(egn)
                        iban=input("Enter an account's IBAN: ")
                        amount=input("How much would you like to withdraw?: ")
                    
                        try:
                            amount=float(amount)
                        except:
                            raise InvalidAccountData("Amount")
                        if amount>0:

                            bank.withdrawal(egn, iban, amount)
                        else:
                            raise InvalidAccountData("Negative amount")
                    else:
                        raise UserNotFound()


                elif choice == "7":
                    print("Goodbye\n")
                    break

                else:
                    raise InvalidMenuChoice()
            except Exception as ex:
                print(f"Error: There was an error while executing the command:\n{str(ex)}")
            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()