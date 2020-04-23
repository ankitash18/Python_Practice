class CheckOut:

    def __init__(self):
        self.prices ={}
        self.total = 0

    def addDiscount(self, item, nbrofitems,price):
        pass


    def addItemPrice(self,item,price):
        self.prices[item] = price

    def additem(self,item):
        self.total += self.prices[item]

    def calculatetotal(self):
        return self.total

