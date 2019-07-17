# Your task is to create a Vampire class that stores a list of vampires (a coven, if you will). 
# Every vampire has a name, age, an in_coffin boolean, and a drank_blood_today boolean.

# Every day at sunset the vampires leave their coffins in search of blood. If they don't drink blood and get back to their coffins before sunrise, they die.

# Your class should have the following methods:

# __init__, which creates a new vampire and assigns values for each of its attributes
# create, which creates a new vampire and adds it to the coven
# drink_blood, which sets a vampire's drank_blood_today boolean to true
# sunrise, which removes from the coven any vampires who are out of their coffins or who haven't drank any blood in the last day
# sunset, which sets drank_blood_today and in_coffin to false for the entire coven as they go out in search of blood
# go_home, which sets a vampire's in_coffin boolean to true
# It's up to you to determine whether each method should be a class method or an instance method, as well as deciding what class and instance variables you need.

# If you're not sure whether a method should be an instance method of a class method, starting to write the body of the method may help you figure it out based on what data you need access to. If you're still uncertain, don't be afraid to ask an instructor to help you work through the problem.

# Good luck!


class Vampire:
    coven = []
    def __init__(self,name, age, in_coffin = True, drank_blood_today = True):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today
    @classmethod
    def create(cls,name, age):
        new_vamp = Vampire(name, age)
        cls.coven.append(new_vamp)
        return(new_vamp)
    
    def drink_blood(self):
        print(f'{self.name} has fed tonight')
        self.drank_blood_today = True
    @classmethod
    def sunset(cls):
        for vamp in cls.coven:
            vamp.in_coffin = False
            vamp.drank_blood_today = False
    @classmethod
    def sunrise(cls):
        for vamp in cls.coven:
            if vamp.in_coffin == False or vamp.drank_blood_today == False:
                cls.coven.remove(vamp)
                print(f'{vamp.name} has been removed from the coven')
    def go_home(self):
        print(f'{self.name} has returned to their coffin')
        self.in_coffin = True

dracula = Vampire.create('Dracula', 100)
alucard = Vampire.create('Alucard', 130) 
viktor = Vampire.create('Viktor', 237)

Vampire.sunset()
dracula.drink_blood()
alucard.drink_blood()

alucard.go_home()

Vampire.sunrise()