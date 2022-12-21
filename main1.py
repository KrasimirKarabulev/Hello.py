from errors import InvalidCommand, InvalidDataFormat, InvalidCharacterClass
from entities import Character
class Menu:
    def __init__(self) -> None:
        self.list_of_character = []
    def print_commands(self):
        print("1. Create a new character")
        print("2. Create a weapon for an existing character")
        print("3. Create a bonus weapon for an existing character")
        print("4. Print all characters")
        print("5. Delete a character")
        print("6. Exit")
    def run(self):
        
        while True:
            
            self.print_commands()
            choice = input("Choose an item from the menu: \n> ")
            
            try:
                
                if choice == "1":
                    
                    name = input("Enter a character name: ")
                    if len(name)<4:
                        raise InvalidDataFormat()
                    
                    sex = input("Enter a character's sex: ")       
                    if len(sex)<4 or not sex.isalpha():
                        raise InvalidDataFormat()
                    
                    klass = input("Enter a character's class: ")
                    klass=klass.upper()
                    
                    if klass!="WARRIOR" and klass!="MAGE" and klass!="ROGUE" and klass!="PRIEST":
                        raise InvalidCharacterClass()
                    
                    charc = Character(name, sex, klass)
                    self.list_of_character.append(charc)
                    
                elif choice == "2":
                    pass
                elif choice == "3":
                    pass
                elif choice == "4":
                    for i in self.list_of_character:
                        print(i.print())
                elif choice == "5":
                    pass
                elif choice == "6":
                    print("End of session")
                    break
                
                else:
                    raise InvalidCommand()
            except Exception as e:
                print(f"Error: {str(e)}")
                
if __name__=="__main__":
    menu = Menu()
    menu.run()
        