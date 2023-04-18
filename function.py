#Function like a script with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    
 #Function with two arguments   
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))
 
 #Function with one argument   
def print_one(arg1):
    print("arg1: %r" % arg1)

#Function with no argument  
def print_none():
    print("I got nothing\n")
    
print_two("Ini", "Blessing")
print_two_again("ini", "Blessing")
print_one("first")
print_none()


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")
    
print("We can just give the function number directly:")
cheese_and_crackers(20, 30)
    
print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
    
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
    
print("We can even do math inside:")
cheese_and_crackers(10 + 20, 5 + 6)
    
print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 25)

print("How many cheese did you eat?")
cheese = input()

print("How many boxes of crackers did you eat?")
crackers = input()

cheese_no = int(cheese)
crackers_no = int(crackers)

cheese_and_crackers(cheese_no, crackers_no)
