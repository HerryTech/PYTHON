class Parent():
    
    def implicit(self):
        print("Inheritance practice")
        
class Child(Parent):
    pass #Create an empty pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


class Parent():
    
    def override(self):
        print("Parent override")
        
class Child(Parent):
    
    def override(self):
        print("Child override")
        
dad = Parent()
son = Child()

dad.override()
son.override()