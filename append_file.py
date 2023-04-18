print("Enter your filename")
filename = input("> ")

print("We are opening %s" % filename)
target = open(filename, "a")

print("Do you have anything you want to append to it?")
append_txt = input("Apend it: ")
target.write("\n")
target.write(append_txt)

print("Cool right? Goodbye")
target.close()