from sys import exit
from random import randint

class Scene:
    def enter (self):
        print("This scene is yet to be configured. Subclass it and implement enter().")
        exit(1)

class Engine:
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = [
        "You died",
        "Game over"
    ]
    
    def enter(self):
        print("Death.quip[randit(0, len(self.quip) - 1 )]")
        exit(1)
    
class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an")
        print("escape pod")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print("a Gothon jumps out. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")
        print("Will you shoot, dodge or tell a joke?")
        
        action = input("> ")
        
        if(action == "shoot"):
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("You missed the shot. He jumps at you in the face")
            return "death"
        
        elif(action == "dodge"):
            print("Like a world class boxer you dodge, weave, slip and slide.")
            print("You bang your head on the metal wall and pass out.")
            print("The gothon stomps on your head")
            return "death"
        
        elif(action == "tell a joke"):
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know")
            print("The Gothon stops, tries not to laugh, then busts out laughing and can't move.")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapon Armory door.")
            return "laser_weapon_armory"
            
        else:
            print("DOES NOT COMPUTE, GO AGAIN!")
            return "central_corridor"
            
    
class LaserWeaponArmory(Scene):
    def enter(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons that might be hiding. It's dead quiet, too quiet")
        print("You stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb. The code is 3 digits.")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[Keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print("BZZZZZEDDD!")
            guesses += 1
            guess = input("[Keypad]> ")
            
        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return "the bridge"
        
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the")
            print("ship from their ship")
            return "Death"
            
    
class TheBridge(Scene):
    def enter(self):
        pass
    
class EscapePod(Scene):
    def enter(self):
        pass
    
class Map:
    
    def __init__(self, start_scene):
        pass
    
    def next_scene(self, scene_name):
        pass
    
    def opening_scene(self):
        pass
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()