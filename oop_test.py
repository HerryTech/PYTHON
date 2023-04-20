import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

PHRASES = {
    "class %%%(%%%):": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef__init__(self ***)": "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
    
#Load up the word from the website
for word in urlopen(word_url).readlines():
    words.append(word.strip())
    
#print(words)

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    other_names = random.sample(words, snippet.count("***"))
    results = []
    param_names = []
    
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(", ".join(random.sample(str(words), param_count)))
        
    for sentence in snippet, phrase:
        result = sentence[:]
        
        #fake class names
        for word in class_names:
            result = result.replace("%%%", str(word), 1)
        
        #fake other names
        for word in other_names:
            result = result.replace("***", str(word), 1)
        
        #fake parameter list
        for word in param_names:
            result = result.replace("@@@", str(word), 1)
        
        results.append(result)
    
    return results

#Keep going until they hit ctrl-C
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        
        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
                
            print(question)
            
            input("> ")
            print("ANSWER: %s\n\n" % answer)
except EOFError:
    print("\nBye")
                
                