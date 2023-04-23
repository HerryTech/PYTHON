def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b #It makes it possible to assign the value to a variable

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with functions!")

age = add(3, 5) 
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d. Weight: %d, IQ: %d" % (age, height, weight,iq))

def break_words(stuff):
    """This function will break up words""" #documentation comment
    words = stuff.split(" ")
    return words

def sort_words(words):
    """This function will sort words"""
    return sorted(words)

def print_first_word(words):
    """Print first word after popping it off"""
    word = words.pop(0)
    return word

def print_last_word(words):
    """Print first word after popping it off"""
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """Takes in full sentence and return the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of a sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then print the first and last one"""
    words = sort_sentence(words)
    print_first_word(words)
    print_last_word(words)
    
