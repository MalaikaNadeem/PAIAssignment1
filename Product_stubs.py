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
