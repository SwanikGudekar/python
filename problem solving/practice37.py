# Creating a Circle class and defining constructor and methods

class circle:
    
    def __init__(self,r):
        self.r =r
        print(r)

    def Area(self):
        return 3.14*self.r*self.r
    
              

    def Perimeter(self):
        return 2 * 3.14 * self.r
        


c1 = circle(5)

print("Area:",c1.Area())
print("perimeter:",c1.Perimeter())





