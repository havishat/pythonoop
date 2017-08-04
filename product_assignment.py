# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes: Price, Item Name, Weight, Brand, Cost
# Status: default "for sale"

# Methods: Sell, add_tax, return
# Every method that doesn't have to return something should return self so methods can be chained.

class Product(object):
  def __init__(self, price, item_name, weight, brand, cost):
    self.price = price*.065+price
    self.item_name = item_name
    self.weight = weight
    self.brand = brand
    self.cost = cost
    self.status = status = "for sale"
    self.reason = []

  def sell(self): # change status to sold
      self.status = "sold"
      return self

  def add_tax(self): # takes tax a decimal amount as a parameter and returns the price of the item including sales tax
      self.price = (self.price*.065)+self.price
      return self

  def returns(self, reason):    # takes return for reason as parameter and changes status accordingly
      if reason == "like new":
          self.status = "for sale"   # if it's being returned in the box, like new mark it as for sale
      elif reason == "defective": # if the item is being returned because it is defective 
          self.status = "defective"       # change status to defective and change price to 0
          self.price = 0
      elif reason == "used":   # if the box has been opened set status to used and apply a 20% discount
          self.status = "used"
          self.price = self.price-(self.price*.20)
      return self.display_info()
  
  def display_info(self): # show all product details
    print "Product Info"
    print "Brand: " + self.brand
    print "Item Name: " + self.item_name
    print "Weight: " + str(self.weight)
    print "Price: $" + str(self.price)
    print "Cost: $" + str(self.cost)
    return "Status: " + self.status

product1 = Product(2000, "MacBook Pro", "3.4lbs", "Apple", 1700)
product2 = Product(600, "Women's Bag", "4lbs", "Marc by Marc Jacobs", 430)

# print product1.display_info()
# print product2.display_info()
print product1.returns("defective")
print product2.returns("used")
# product1.returns("defective")
# product2.returns("used")
# print product1.display_info()