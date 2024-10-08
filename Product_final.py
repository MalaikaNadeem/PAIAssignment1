# SP23-BAI-008
# SP23-BAI-024

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        
    def get_price(self, quantity):     
          if quantity < 0:
              raise ValueError('Invalid Quantity')
          else:
              if quantity < 10:
                  total_cost = (self.price*quantity)
              elif quantity >= 10 and quantity < 100:
                  discount = (self.price *10)/100
                  total_cost = (self.price - discount) * quantity
              else:
                  discount = (self.price *20)/100
                  total_cost = (self.price - discount) * quantity
        
          return total_cost
      
      
    def make_purchase(self, quantity):
          if quantity > self.amount:
              raise Exception("Sorry, you requested more products than available.")
          else:
              self.amount = self.amount - quantity
              totalPrice = self.get_price(quantity)
              print("The total price charged is: " + str(totalPrice))
try:
    product1 = Product("Mobile", 10, 100000)
    product1.make_purchase(10)
    product1.make_purchase(5)
    
    product2 = Product("Laptop", 20, 200000)
    product2.make_purchase(25)
    
    product2 = Product("Pc", 100 , 10002000)
    product2.make_purchase(-2)
except Exception as e:
    print(f"Error: {e}")



  

