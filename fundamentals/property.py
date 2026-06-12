class Student:

    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"


s1 = Student(98, 91, 94)

print(s1.percentage)

s1.phy = 90
print("physics chnaged marks:",s1.phy)

print(s1.percentage)