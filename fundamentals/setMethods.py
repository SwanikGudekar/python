collection = set() # created an emty set

# used to add element in set
collection.add(1)
collection.add(2)
collection.add("hello")

print("add ",collection)

# remove elements form set 
collection.remove(2)
print("remove ",collection)

# used the reomve a random element
collection.pop()
print("pop ",collection)

# used to remove all element form the list
collection.clear()
print("clear all element",collection)
print("length ",len(collection))


set1={1,2,3,4}
set2={1,5,6,7}

# union cobine both set and return a new set
print("union",set1.union(set2))

#intersection combine common element
print("intersection",set1.intersection(set2))
