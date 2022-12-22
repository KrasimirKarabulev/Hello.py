from .items import Item

class Weapon(Item):
    def __init__(self, name, attack) -> None:
        super().__init__(name)
        self.attack=attack
    
    def print(self):
        return f"Type: {self.name}, Attack: {self.attack}, Durability: {self.durabity}"