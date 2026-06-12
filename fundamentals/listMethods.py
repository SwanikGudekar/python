age = [21,41,32,10]
print("orginal",age)

#append is to add a elemnt at the end
age.append(58)
print("append",age)

#sort is used to sort the list is asending order
age.sort()
print("sort",age)

#sort reverse is used to sort in decending order 
age.sort(reverse=True)
print("reverse sort",age)

# insert is used to add a element in a particular index
age.insert(3,22)
print("insert",age)

# reverse is used to reverse the list
age.reverse()
print("reverse",age)

# remove is used to remove a element form the list
age.remove(58)
print("remove",age)

# pop is used to remove a element from a particular index
age.pop(2)
print("pop",age) 