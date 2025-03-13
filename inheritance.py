class animal:
    def __init__(self,name,body_temp,body):
        self.name = name
        self.body_temp = body_temp
        self.body = body
        
    def properties(self):
        print(f"{self.name} is {self.body_temp} and it's body has {self.body}")
        
class bird(animal):
    def __init__(self,name,body_temp,body,movement):
       super().__init__(name,body_temp,body)
       self.movement = movement
    
    def properties(self):
        super().properties()
        print(f"movement : {self.movement}")
        
class fish(animal):
    def __init__(self,name,body_temp,body,movement):
        super().__init__(name,body_temp,body)
        self.movement = movement
    
    def properties(self):
        super().properties()
        print(f"movement : {self.movement}")
        
bird = bird("eagle","warm blooded","feathers","flying")
fish = fish("tilapia","cold blooded","scales","swimming")

#print(bird.body_temp)
bird.properties()  
fish.properties()
        