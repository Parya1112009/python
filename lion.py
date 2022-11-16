class lion(cat):
    def __init__(self,name):
        self.name = name
    def roars(self):
        print(f"{self.name} roars")
sharkhan = lion("sherkhan")
sherkhan.meows()
sherkhan.roars()
