class Student:
    college_name="sigce" # same for all object

    def __init__(self,name,marks): #constructor
        self.name = name # self.name means that all object name is diffrent
        self.marks = marks
        
# objects
s1 = Student("swanik","84") # here swanik and 84 are called attributes
print(s1.name,s1.marks)
print(s1.college_name)

s2=Student("ojas",95)
print(s2.name,s2.marks,s2.college_name)

