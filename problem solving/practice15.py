#WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks ={}

a = int(input("enter the enter marks of physics: "))
marks.update({"physics": a})

b = int(input("enter the enter marks of chemistry: "))
marks.update({"chemistry": b})

c = int(input("enter the enter marks of maths: "))
marks.update({"maths": c})

print(marks)


