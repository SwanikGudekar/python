# create student class that takes names and marks of 3 subject as an argument as an constructor and print thir average

class Student:

    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 =marks1
        self.marks2 =marks2
        self.marks3 =marks3


    def average(self):
        avg= (s1.marks1+s1.marks2+s1.marks3)/3
        print(s1.name,"your average is",avg)

s1 =Student("swanik",81,83,88)
s1.average()