class cat:
    def __init__(self,name):
        self.name = name
        print("Inside cat init")
    def meows(self):
        print(f"{self.name} meows")
kitty = cat("kitty")
kitty.meows()
class lion(cat):
    def __init__(self,name,pride_name):
        super().__init__(name)
        self.pride_name = pride_name
        print("inside lion class") 
    def roars(self):
        print(f"{self.name} roars")
sherkhan = lion("sherkhan","raja")
sherkhan.meows()
sherkhan.roars()
