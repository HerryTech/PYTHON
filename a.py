from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    next = input("> ")
    
    if next.isdigit():
        how_much = int(next)
    else:
        print("I'll repeat the question, type in a number!")
        gold_room()
        
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        game_over("You are greedy.")
        
def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("What would you do, take the honey or taunt the bear?")
    
    while True:
        next = input("> ")
        
        if next == "take the honey":
            game_over("The bear looks at you then slaps your face.")
        elif next == "taunt the bear":
            print("The bear has moved from the door, open the door and go through it now")
        elif next ==  "open the door":
            gold_room()
        else:
            print("I got no idea what that means")
            
def big_room():
    print("Here you see a big gorilla")
    print("It's staring at you")
    print("Do you flee for your life or try to kill it")
    
    next = input("> ")
    
    if "flee" in next:
        print("No escape route, you have to start again")
        start()
    elif "kill" in next:
        game_over("That won't be an easy one, you tried champ!.")
    else:
        big_room()
    
def game_over(why):
    print(why, "Good bye!")
    exit(0)
    
def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take?")
    
    next = input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        big_room()
    else:
        print("It's not part of the option. Start again!")
        start()
        
start()