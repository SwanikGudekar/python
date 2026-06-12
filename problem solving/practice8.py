# program to check gretest number entered by user

a =int(input("enetr first number: "))
b =int(input("enetr second number: "))
c =int(input("enetr third number: "))

if(a >b and a> c):
    print(a,"is greater")

elif(b>a and b>c):
    print(b,"is greater")

else:
    print(c,"is greater")