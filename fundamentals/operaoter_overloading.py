class Complex:

    def  __init__(self,img,real):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,n2):  #__add__ is a dunder function
        newReal = self.real +n2.real
        newImg =self.img+n2.img
        return Complex(newReal,newImg)

n1 = Complex(4,6)
n1.showNum()

n2 =Complex(7,9)
n2.showNum()

n3 = n1+n2
n3.showNum()