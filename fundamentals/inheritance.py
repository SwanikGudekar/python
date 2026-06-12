# single level inheritance

class Car: # base class

    def Start(self):
        print("car started")

    def stop(self):
        print("car stoped")

class Toyota(Car): # toyota is inherited class of car

    def __init__(self,name):
        self.name = name

c1 = Toyota("Fortuner")

print(c1.name) # inherited class object
print(c1.Start()) # base class object