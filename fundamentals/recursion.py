# print n to 1 backward

def num(n):
    if(n==0):
        return
    print(n,end =" ")
    num(n-1)

num(5)
