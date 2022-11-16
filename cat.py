class cat:
    def __init__(self,name):
        self.name = name
    def meows(self):
        print(f"{self.name} meows")
kitty = cat("kitty")
kitty.meows()
class lion(cat):
    def __init__(self,name):
        self.name = name
    def roars(self):
        print(f"{self.name} roars")
sherkhan = lion("sherkhan")
sherkhan.meows()
sherkhan.roars()
