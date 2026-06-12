# multilevel inhertance

class Car: # 1 class (base class)

    def Start(self):
        print("car started")

    def stop(self):
        print("car stoped")

class Toyota(Car): # 2 class (child class)

    def __init__(self,brand):
        self.brand = brand


class Fortuner(Toyota): # 3 class(child class)
    
    def __init__(self,type,brand):
        self.type = type
        super().__init__(brand) # This is super method # Call Toyota constructor 


c1 = Fortuner("Toyota","Disel")
print(c1.type) # if we want to print attribute then dont put()
print(c1.brand)
print(c1.Start()) # base class object # if we want to print methd then only put()