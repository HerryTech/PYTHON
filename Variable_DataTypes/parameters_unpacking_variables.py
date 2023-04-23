from sys import argv #argv = argument variables

script, first, second, third = argv #unpacking
fourth = input("What is your fourth variable? ")

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

print ("All together, your script is called %s, your first variable is %s, your second is %s, your third is %s, and your fourth is %s" % (script, first, second, third, fourth))

print(argv)