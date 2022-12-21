from .item import Item

class Weapon(Item):
    def __init__(self, type, attack) -> None:
        super().__init__(type)
        self.attack=attack