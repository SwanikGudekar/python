#create a class order which store item and its price
#use dunder function (__gt__)  to convey that : order 1 > order2  if the price of order1> order2

class Order:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    def Demo(self):
        print(self.item)
        print(self.price)

    def __gt__(self,o2): # dunder function
        return self.price>o2.price

o1 =Order("Ball",150)
o2=Order("Bat",2000)
print("Order 1:")
o1.Demo()
print("Order 2:")
o2.Demo()
print("Is order 1 is expensive then order2:",o1>o2) 
