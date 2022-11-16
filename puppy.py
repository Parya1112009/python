class Dog:
    def __init__(self,name,breed,location):
        self.name = name
    	self.breed = breed
  	self.location = location
    	self.tricks = []
    def bark(self):
	print("says woff")
otter = Dog("otter", "Husky","fremont")
otter.bark()
#print (otter.name)
#print (otter.breed)
#print (otter.location)
#print (otter.tricks)
#print("#########another instance#############")
#jules = Dog("jules", "chihu","sanjose")
#print (jules.name)
#print (jules.breed)
#print (jules.location)
