class InvalidCommand(Exception):
    def __init__(self, message = "Entered command is invalid", *args: object) -> None:
        super().__init__(message,*args)
        
class InvalidDataFormat(Exception):
    def __init__(self, name, *args: object) -> None:
        message = f"Invalid data format: {name}"
        super().__init__(message, *args)
        
class CharacterExists(Exception):
    def __init__(self, message = "Entered character already exists",*args: object) -> None:
        super().__init__(message, *args)
        
class InvalidCharacterClass(Exception):
    def __init__(self, message = "Invalid character class",*args: object) -> None:
        super().__init__(message, *args)
        
class CharacterNotFound(Exception):
    def __init__(self, message = "Entered character was not found", *args: object) -> None:
        super().__init__(message, *args)