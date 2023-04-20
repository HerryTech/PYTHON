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
        else:
            print("DOES NOT COMPUTE!")
            return "central_corridor"
            
    
class LaserWeaponArmory(Scene):
    def enter(self):
        pass
    
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