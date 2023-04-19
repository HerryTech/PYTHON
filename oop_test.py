import random
from urllib import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%"
    "class %%%(object):\n\tdef__init__(self ***)"
     "class %%% has-a __init__ that takes self and *** parameters."
    "class %%%(object):\n\tdef ***(self, @@@)"
     "class %%% has-a function named *** that takes self and @@@ parameters."
    "***= %%%()"
     "Set *** to an instance of class %%%."
    """***.***(@@@):"""
    "From *** get the *** function, and call it with parameters self, @@@."
    """***.*** = '***'":"""
      "From *** get the *** attribute and set it to '***'."
}

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
    
#Load up the word from the website
for word in urlopen(word_url).readlines():
    words.append(word.strip())
    
print(words)