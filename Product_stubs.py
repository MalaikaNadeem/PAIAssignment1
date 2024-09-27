class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        return 1000

    def make_purchase(self, quantity):
        if quantity > self.amount:
            raise Exception("Sorry, you requested more products than available.")
        else:
            self.amount = self.amount - quantity
            totalPrice = self.get_price(quantity)
            print("The total price charged is: " + str(totalPrice))