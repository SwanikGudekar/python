# find the factorial of n using function
 


def fac(n):
    facto = 1
    for i in range (1,n+1):
        facto *= i
        print (facto, end =" ") 


fac(5)