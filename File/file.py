filename = "./File/exp2.txt"

txt = open(filename)

print("Here is your file %r" % filename)
print(txt.read())
txt.close()

print("Type the filename again")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()