"""
for in
slice
min, max, sum
list(range())
"""
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician)
    print(f"{magician.title()}, that was a great trick!")

print("\nThank you, everyone. That was a great magic show!")

print("-" * 10)

for value in range(1, 5):
 print(value)
 
numbers = list(range(1, 6))
print(f"\n{numbers}")

even_numbers = list(range(2, 11, 2)) 
print(f"\n{even_numbers}")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
