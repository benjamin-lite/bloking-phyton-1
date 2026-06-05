class car : 
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")

class boat :
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("sail")

class plane : 
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")

carl = car("ford", "mustang")       #create a car class
boatl = boat("Ibiza", "touring 20") #create a boat class
planel = plane("boeing", "747")     #create a plane class

for x in (carl, boatl, planel):
    x.move

    
