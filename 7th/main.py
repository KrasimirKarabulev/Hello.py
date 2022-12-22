from errors import InvalidCommand, InvalidDataFormat, InvalidCharacterClass, CharacterNotFound, CharacterExists
from entities import Character, Weapon, Item
class Menu:
    def __init__(self) -> None:
        self.list_of_character = []
    def print_commands(self):
        print("1. Create a new character")
        print("2. Create a weapon for an existing character")
        print("3. Create a bonus item for an existing character")
        print("4. Print all characters")
        print("5. Delete a character")
        print("6. Exit")

    def check_for_char(self, name):
        for i in self.list_of_character:
            if name==i.name:
                return name
        return None

    def run(self):
        
        while True:
            print(" ")
            self.print_commands()
            choice = input("Choose an item from the menu: \n> ")
            
            try:
                
                if choice == "1":
                    
                    name = input("Enter a character name: ")
                    for char in self.list_of_character:
                        if name==char.name:
                            raise CharacterExists()

                    if len(name)<4:
                        raise InvalidDataFormat("name")
                    
                    sex = input("Enter a character's sex: ")       
                    sex = sex.upper()
                    klass = input("Enter a character's class: ")
                    klass=klass.upper()
                    charc = Character(name, sex, klass)

                    self.list_of_character.append(charc)
                    
                elif choice == "2":
                    name = input("Enter an existing character's name: ")
                    char_found=False
                    for char in self.list_of_character:
                        if name == char.name:
                            char_found=True
                            wep_type=input(("Enter the type of weapon: "))
                            wep_type=wep_type.upper()
                            if type(wep_type)!=str or len(wep_type)<4:
                                raise InvalidDataFormat("type")

                            wep_attack=input(("Enter the attack power of the weapon: "))
                            try:
                                wep_attack=int(wep_attack)
                            except:
                                raise InvalidDataFormat("attack")
                        
                            if wep_attack<0:
                                raise InvalidDataFormat("attack")
                            
                            weapon = Weapon(wep_type, wep_attack)
                            char.equip_weapon(weapon)
                            print("Complete")
                    if not char_found:     
                        raise CharacterNotFound()

                elif choice == "3":
                    name = input("Enter an existing character's name: ")
                    char_found=False
                    for char in self.list_of_character:
                        if name == char.name:
                            char_found=True
                            item_type=input(("Enter the type of item: "))
                            item_type=item_type.upper()
                            if type(item_type)!=str or len(item_type)<4:
                                raise InvalidDataFormat("type")

                            item = Item(item_type)
                            char.equip_item(item)
                            print("Complete")
                    if not char_found:     
                        raise CharacterNotFound()

                elif choice == "4":
                    for i in self.list_of_character:
                        print(i.print())


                elif choice == "5":
                    name = input("Enter an existing character's name: ")
                    char_found=False
                    for char in self.list_of_character:
                        if name==char.name:
                            char_found=True
                            self.list_of_character.remove(char)

                    if not char_found:
                        raise CharacterNotFound()

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