from errors import CharacterExists, InvalidCharacterClass, CharacterNotFound, InvalidDataFormat
class Character:
    char_klasses=["PRIEST", "WARRIOR", "ROGUE", "MAGE"]
    char_sexes=["MALE", "FEMALE"]
    def __init__(self, name, sex, klass) -> None:
        if klass not in Character.char_klasses:
            raise InvalidCharacterClass()
        if sex not in Character.char_sexes:
            raise InvalidDataFormat("sex")
        self.name=name
        self.sex=sex
        self.klass=klass
        self.weapon=None
        self.item=None
        
    def print_characters(self, array):
        for i in array:
            print(f"Name: {self.name}, Sex: {self.sex}, Class: {self.klass}")
            
        
    def print(self):
        weapon_info = "None"
        item_info = "None"
        if self.weapon!=None:
            weapon_info=self.weapon.print()
        if self.item!=None:
            item_info=self.item.print()
        return f"Name: {self.name}, Sex: {self.sex}, Class: {self.klass}, Weapon: [{weapon_info}], Item: [{item_info}]"
    
    def equip_weapon(self, weapon):
        self.weapon=weapon

    def equip_item(self, item):
        self.item=item

    