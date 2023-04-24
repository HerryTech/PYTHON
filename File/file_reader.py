import fileinput
with open("./File/exp2.txt") as file_object:
    content = file_object.read()
print(content.strip()) 

print("-" * 10)

filename = "./File/exp2.txt"

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

filename = "./File/pi.txt"
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

with fileinput.input(files=("File\exp2.txt", "File\guest_book.txt")) as f: #open multiple files at once
    for line in f:
        print(line)