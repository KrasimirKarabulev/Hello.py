class Item:
    def __init__(self, name) -> None:
        self.name = name
        self.durabity= 100

    def print(self):
        return f"Type: {self.name}, Durability: {self.durabity}"