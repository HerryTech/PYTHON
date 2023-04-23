from name_function import get_formatted_name

print("Enter 'q' at anytime to quit")

while True:
    firstname = input("What is your first name?: ")
    if firstname == "q":
        break
    lastname = input("What is your last name?: ")
    if lastname == "q":
        break
    else:
        formated_name = get_formatted_name(firstname, lastname)
        print(f"Neatly formatted name: {formated_name}")