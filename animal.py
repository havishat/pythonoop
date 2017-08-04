#Assignment: Animal
#Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self): #walk: decreases health by one
        self.health -= 1
        return self

    def run(self): #run: health decreases by five
        self.health -= 5
        return self

    def display_health(self): # display health: print to the terminal the animal's health.
        print "my name " + self.name
        print "I have: " + str(self.health) + " health"
#Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.
animal = Animal('lion', 100)
animal.walk().walk().walk().run().run().display_health()

class Dog(Animal): # inherits everything from Animal
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150 #pet: increases health by 5
    def pet(self): 
        self.health += 5  #pet: increases health by 5
#Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
Dog = Dog("jojo", 150)
Dog.walk().walk().walk().run().run().display_health()

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170 #default health of 170

    def fly(self):
        self.health -= 10 #fly: decreases health by 10
        return self

    def display_health(self): # display health: prints health by calling the parent method and prints "I am a Dragon"
        print "I am a Dragon"
        super(Dragon, self).display_health()

dragon = Dragon('Nightwing', 120)
dragon.fly().display_health()

animal = Animal('cat', 60) 
animal.walk().walk().walk().run().run().display_health()
#animal.pet() ...Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().











    
        