my_name = "Ilesanmi Blessing"
my_age = 25
my_height = 56 #inches
my_weight = 55 #kg
my_eyes = "black"
my_teeth = "white"
my_hair = "black"

print("Let's talk about %s" % my_name)
print("She is %d years old" % my_age)
print("She is %d inches tall" % my_height)
print("She is %d kg heavy" % my_weight)
print("Actually, that's not too heavy")
print("She has %s eyes and %s hair" % (my_eyes, my_hair))
print("Her teeth are usually %s depending on the coffee" % my_teeth)
print("If I add %d, %d and %d I get %d" %(my_age, my_height, my_weight, my_age + my_height + my_weight))

#You can use %r, this means "print it no matter what"

#conversion
height = 56 #inches
my_height = height * 2.54

print("She is %d cm tall" % my_height)