filename = "./File/exp2.txt"

with open(filename, "a") as file:
    file.write("You can learn it also\n")
    
filename = "./File/w.txt"
with open(filename, "w") as file:
    file.write("This is just for practice\n")
    file.write("Keep up the good work")

#name = input("What is your name? ")

#with open("./File/guest.txt", "w") as name_file:
    #name_file.write(name)
    
    while True:
        name = input("What is your name? ")
        print(f"Welcome, {name}")
        with open("./File/guest_book.txt", "a") as name_file:
            name_file.write(f"{name}, vsited our website\n")
        