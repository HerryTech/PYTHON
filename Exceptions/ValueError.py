print("Do you want to add two numbers?")
print("Enter the numbers")
print("or enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if first_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
        print(answer)
    except ValueError:
        print("NOT A NUMBER!. Type in numbers")
    
    