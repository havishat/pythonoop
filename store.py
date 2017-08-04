import numpy as np

class store(object):
    def __init__(self, products, location, owner):
        self.products = products
        #self.products = np.array["pen", "brush", "apple", "cap"]
        self.location = location
        self.owner = owner
        self.display_info()
       # print self.products
        
    def add_product(self):
        self.products.append("book")
        return self
    
    def remove_product(self):
        self.products.remove('brush')
        return self

    def inventory(self):
        self.inventory = self.products
        return self

    def display_info(self): # show all product details
        print "store Info"
        print "prodcut" + str(self.products)
        print "location" + str(self.location)
        print "owner" + str(self.owner)

    def __str__(self):
        return "Products ( {} ) Location ( {} ) Owner ( {} )".format(' '.join(self.products), self.location, self.owner)   

store1 = store(["apple", "brush", "store"],"47 zanker","havisha")
print store1
print store1.add_product() 
print store1.remove_product() 
print store1.inventory()
