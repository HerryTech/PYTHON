print("You enter a dark room with two doors. Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating cheese cake. What do you do?")
    print("1: Take the cake")
    print("2: Scream at the bear")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away" % bear)
        
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1: blueberries")
    print("2: Yellow jacket clothespins")
    print("3: Understanding revolvers yelling melodies")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survived. Good job!")
    else:
        print("You have to run!")
        
else:
    print("You have to pick a number. Either 1 or 2")