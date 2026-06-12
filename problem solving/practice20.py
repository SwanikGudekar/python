# find x in the tupple
#(1,4,9,16,25,36,49,64,81,100)

nums =(1,4,9,16,25,36,49,64,81,100)
i = int(input("enter the square number from 1 to 10: "))
idx=0
while idx<len(nums):
    if(nums[idx]==i):
        print("found number at index: ",idx)
        break;
    else:
        print("not found")
    idx +=1
