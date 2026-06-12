# find a number in a tuple

tup =(1,4,9,16,25,36,49,64,81,100)

idx = 0
i = int(input("Enter a number: "))
for num in tup:
        if(i == num):
            print(i, "found at idx",idx)
            break        
        idx += 1
       