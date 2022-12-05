import random
class MissingParameterError(Exception):
    pass
class InvalidParameterError(Exception):
    def __init__(self, name):
        message = f"Invalid class parameter: {name}"
        super().__init__(message)
        
class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")
       

class InvalidSoundError(InvalidParameterError):
     def __init__(self):
        super().__init__("sound")

class JungleAnimal():
    def __init__(self, name=None, age=None, sound=None):
        self.name=name
        self.age=age
        self.sound=sound
        if name == None or age==None or sound==None:
            raise MissingParameterError()
        if type(name)!= str:
            raise InvalidParameterError("name")
        if type(age)!=int:
            raise InvalidAgeError()
        if type(sound)!=str:
            raise InvalidSoundError()

    def make_sound(self):
        print(f"{self.name} says {self.sound}")
        
    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age >15:
            raise InvalidAgeError()
        r_count=0
        
        for i in sound:
            if i=="r" or i=="R":
                r_count+=1
        if r_count<2:
            raise InvalidSoundError()    
    
    def print(self):
        return print(f"Jaguar ({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals = []):
        for i in range(len(animals)-1):
            if type(animals[i])==Human or type(animals[i])==Lemur:
                animal = animals[i]
                print(f"{self.name}, the Jaguar hunter down {animal.name} the {type(animal).__name__}")
                del animals[i]
                break
                
                
class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age>10:
            raise InvalidAgeError()
        if "e" not in sound:
            raise InvalidSoundError()
    def print(self):
        return print(f"Lemur({self.name}, {self.age}, {self.sound}")

    def daily_task(self, count):
        if count>=10:
            print(f"{self.name}, the Lemur ate a full meal of 10 fruits")
            count=count-10
            return count

        elif count<=0:
            self.make_sound()
            print(f"{self.name}, the Lemur couldn't find anything to eat")
            self.make_sound()
            print(f"{self.name}, the Lemur couldn't find anything to eat")
            return 0

        elif count<10:
            print(f"{self.name}, the Lemur could only find {count} fruits")
            return 0
        
class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if age>10:
            raise InvalidAgeError()
        if "e" not in sound:
            raise InvalidSoundError()
    
    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")
    
    def daily_task(self, animals, buildings):
        for i in range(len(animals)-1):
            if type(animals[i])==Human:
                if i==0:
                    if type(animals[i+1])==Human:
                        building = Building(animals[i], animals[i+1])
                        buildings.append(building)
                elif i==len(animals)-1:
                    if type(animals[i-1])==Human:
                        building = Building(animals[i-1], animals[i])
                        buildings.append(building)
                elif type(animals[i-1])==Human and type(animals[i+1])==Human:
                    building = Building(animals[i-1], animals[i], animals[i+1])
                    buildings.append(building)
            

class Building():
   
    def __init__(self, *type1):
        self.type=type1


fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    y=random.randint(0,9)
    name=names[random.randint(0, len(names)-1)]
    age= random.randint(0,20)
    sound =sounds[random.randint(0, len(sounds)-1)]
    animal=0
    try:
        if y>=0 and y<=3:
            animal=Lemur(name, age, sound)
            

        elif y>3 and y<=7:
            animal=Jaguar(name, age, sound)
           

        elif y>7 and y<=9:
            animal=Human(name, age, sound)

        animals.append(animal)
    except Exception as e:
       print(f"{y} {name} {age} {sound} {e}")
   
print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim)==Jaguar:
        anim.daily_task(animals)
    elif type(anim)==Lemur:
        fruits = anim.daily_task(fruits)
        
    elif type(anim)==Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)

