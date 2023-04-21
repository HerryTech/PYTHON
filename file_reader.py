from sys import argv

script, filename = argv

txt = open(filename)

print("Here is your file %r" % filename)
print(txt.read())
txt.close()

print("Type the filename again")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

print("-" * 10 )

with open("exp2.txt") as file_object:
    content = file_object.read()
print(content.strip()) 

print("-" * 10)

filename = "exp2.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
        
print("-" * 10)

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

file = ''  
for line in lines:
    file += line.strip()
    print(file)
    
    
print(f"{file[20:]}") 


print(file)
print(f"{file[:20]}") 
print(len(file))

print("-" * 10)

filename = "pi.txt"
pi_string = ""

with open(filename) as pi:
    lines = pi.readlines()

for line in lines:
    pi_string += line.strip()
    
    
print(f"{pi_string[:50]}")

birthday = input("Type in ypur birthday in mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in pi_string")
else:
    print("Your birthday does not appears in pi_string")

