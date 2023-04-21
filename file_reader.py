with open("exp2.txt") as file_object:
    content = file_object.read()
print(content.rstrip()) 

print("-" * 10)
filename = "exp2.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line)
