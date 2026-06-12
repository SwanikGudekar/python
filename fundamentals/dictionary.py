student = {
    "name" : "swanik",
    "age" : 21,
    "year" : "Third",
    "cgpa" : 9.8,
    "is_adult": True,
    "subject": ["python","os","java"]
}

print(student)
print(type(student))
print(student["name"]) # used to acces the value

student["cgpa"] = 8.73 # used to change the value of key
print(student)

student["stream"] = "cybersecurity" # used to add a key and value in dictionary
print(student)