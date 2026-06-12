# print the factorial of n number

fac = 1

for i in range(1,11,1):
    fac *= i
print("Factorial using for loop  is ",fac)

# same using while loop


fact = 1
i = 1
while i<= 10:
    fact *= i
    i+=1
print("factorial using while loop",fact)