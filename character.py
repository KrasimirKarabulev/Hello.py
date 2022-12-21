from errors import CharacterExists, InvalidCharacterClass, CharacterNotFound
class Character:
    char_klasses={"PRIEST", "WARRIORR", "ROGUE", "MAGE"}
    def __init__(self, name, sex, klass) -> None:
        if klass not in Character.char_klasses:
            raise InvalidCharacterClass()
        self.name=name
        self.sex=sex
        self.klass=klass
        self.characters=[]
        
    # def search_for_chacater(self, name):
    #     for i in self.characters:
    #         if i.name==name:
    #             return i
    #     return None
    
    
    def print_characters(self, array):
        for i in array:
            print(f"Name: {self.name}, Sex: {self.sex}, Class: {self.klass}")
            
        
    def print(self):
        return f"Name: {self.name}, Sex: {self.sex}, Class: {self.klass}"
    
        
    