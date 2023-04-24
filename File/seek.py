with open("File\seek.txt", "w") as f:
    f.write("I'm a lady on a tech journey")
    f.write("\nIt has been an amazing journey so far")

with open("File\seek.txt") as f:
        f.seek(6, 0)
        print(f.readline())