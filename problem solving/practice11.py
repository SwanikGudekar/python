# check if a list contain palidrom or not

list = (input("Enter values: "))
print(list)

copy_list =list[:-1]
print(copy_list)


if(list==copy_list):
    print("list is palindrome")
else:
    print("list does not contain palindrome")