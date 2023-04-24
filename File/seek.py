with open("File\seek.txt", "w") as f:
    f.write("I'm a lady on a tech journey.\n")
    f.write("It has been an amazing journey so far")

with open("File\seek.txt") as f:
        f.seek(6, 0)
        print(f.readline())
        
with open("File\seek1.txt", "w") as f:
    f.write("A, B, C, D, E, F, G, H, I, J")
    f.seek(6, 0)
    f.write("Hello")
    
with open("File\seek1.txt", "r") as f:
    lines = f.readline()
    print(lines)
    

    
