class Dog:
    species = 'Canine'
    num_dogs = 0
    def __init__(self,name,breed,location):
        self.name = name
        self.breed = breed
        self.location = location
        self.tricks = []
        Dog.num_dogs += 1
    @classmethod
    def register_stray(cls):
        return cls("unknown","unknown","unknown")
    def bark(self):
        print(f"{self.name} says woff")
    def learn_tricks(self,new_trick):
        if new_trick not in self.tricks:
            self.tricks.append(new_trick)
    def perform_tricks(self,trick):
        if trick in self.tricks:
            print (f"{self.name} performs {trick}")
        else:
            print (f"{self.name} does not know {trick} :(")
stray1 = Dog.register_stray()
print (f"{stray1.name}")
otter = Dog("otter", "Husky", "fremont")
otter.bark()

otter.learn_tricks("sit")
otter.perform_tricks("sit")
otter.perform_tricks("stand")
#print (otter.name)
#print (otter.breed)
#print (otter.location)
#print (otter.tricks)
#print("#########another instance#############")
jules = Dog("jules", "chihu","sanjose")
jules.bark()
jules.learn_tricks("stand")
jules.perform_tricks("stand")
print (f"{jules.tricks}")
#print (jules.name)
#print (jules.breed)
#print (jules.location)
