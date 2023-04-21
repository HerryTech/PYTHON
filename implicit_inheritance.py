class Parent():
    
    def implicit(self):
        print("Inheritance practice")
        
class Child(Parent):
    pass #Create an empty pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()