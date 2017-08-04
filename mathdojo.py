#Assignment: MathDojo
#HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.
#PART I
#Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self, *number):
        for var in number:
            self.result += var
        return self

    def subtract(self, *number):
        for var in number:
            self.result -= var
        return self

md = MathDojo()
print md.add(2).add(2, 5).subtract(3, 2).result

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:

class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *args):
            for x in args:
                if type(x) is list:
                    for i in x:
                        self.result += i
                elif type(x) is int or type(x) is float: 
                    self.result += x
            return self

    def subtract(self, *args):
            for x in args:
                if type(x) is list:
                    for i in x:
                        self.result += i
                elif type(x) is int or type(x) is float: 
                    self.result += x
            return self

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

# PART III
# Make any needed changes in MathDojo in order to support tuples of 
# values in addition to lists and singletons.  
class MathDojo3(object):
	def __init__(self):
		self.result = 0

	def add(self, *args): 
		for x in args:
			if type(x) is int:
				self.result += x
			elif type(x) is list:
				for i in x:
					self.result += i
			elif type(x) is tuple:
				for i in x:
					self.result += i
		return self

	def subtract(self, *args):
		for x in args:
			if type(x) is int or type(x) is float:
				self.result -= x
			elif type(x) is list:
				for i in x:
					self.result -= i
			elif type(x) is tuple:
				for i in x:
					self.result -= i
		return self 

	def result(self):
		print(self.result)

md3 = MathDojo3()
tup = (1,3,4)
print md3.add(tup, [1,2,3], 9, 8, 10).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result