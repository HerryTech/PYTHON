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