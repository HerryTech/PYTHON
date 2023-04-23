"""
sort
sort(reverse = True)
sorted
reverse
len
"""

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #arranges alphabetically
print(cars)

cars.sort(reverse=True) #arrange alphabetically from the back
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nThe reversed list:")
cars.reverse()
print(cars)

number = len(cars)
print(f"\nYou have {number} cars")