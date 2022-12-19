# User
class InvalidUserData(Exception):
    def __init__(self, name, *args: object) -> None:
        message = f"Invalid user data: {name}"
        super().__init__(message, *args)

class UserNotFound(Exception):
    def __init__(self, message = "User is not found", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyExists(Exception):
    def __init__(self, message = "User already exists", *args: object) -> None:
        super().__init__(message, *args)

class UserAlreadyOwnsAccount(Exception):
    def __init__(self, message = "Error: This account already belongs to this user", *args: object) -> None:
        super().__init__(message, *args)
# Account 
class AccountNotFound(Exception):
    def __init__(self, message = "Account is not found", *args: object) -> None:
        super().__init__(message, *args)

class UnsufficientBalance(Exception):
    def __init__(self, message = "Balance of the account is unsifficient", *args: object) -> None:
        super().__init__(message, *args)

class InvalidAccountData(Exception):
    def __init__(self, name, *args: object) -> None:
        message = f"Invalid account data: {name}"
        super().__init__(message, *args)

class InvalidAccountType(Exception):
    def __init__(self, message = "Account type entered is invalid", *args: object) -> None:
        super().__init__(message, *args)
# Bank
# Menu
class InvalidMenuChoice(Exception):
    def __init__(self, message = "Entered menu choice is invalid", *args: object) -> None:
        super().__init__(message, *args)
