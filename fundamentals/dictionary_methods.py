student ={
    "name" :"swanik",
    "age" :21,
    "marks":{
        "chemistry": 78,
        "mathematics" : 89,
        "science":75
    }
}

print(student)

# dic.keys is usedd to return all keys from the dictionary
print("this are keys" ,student.keys()) 

# dic.values is used to return all values
print("this are values",student.values())

# conver to list
print("convert to list",list(student.keys()))

# converts to tuple and return all keys and values
print("convert to tupple",student.items())

# prints length of the dic (means return length of keys)
print("return the length",len(student))

# return the value of the key
print("return the value",student["name"]) # if the key does not exit it will return error
print("return the value using method",student.get("name")) # if the key does not exit it will return none

# add new key and value in the dic
student.update({"city":"mumbai"})
print("update dic is :",student)

# update keys and value in teh  dic
student.update({"name":"swadhin"})
print(student)




