class family:
    attr4 = "choti"
    attr5 = "chotu"
    def __init__(self,attr1,attr2,attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
    def fun(self):
        print ("I'm a", self.attr1)
        print ("I am ", self.attr2)
        print ("I am ", self.attr3)

print("USA family members are here")        
obj = family("ravi","yuvan","eva")
obj1 = family("santosh","rajendra","guddu")
obj.fun()
print("india family members are here")
obj1.fun()
print("india family more members are here",obj1.attr4,obj.attr5)


