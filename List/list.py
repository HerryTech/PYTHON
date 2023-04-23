"""
Append
Insert
Delete
Remove
Pop
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)


print("-" * 10)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

print("-" * 10)

motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)

motorcycles.insert(1, 'ducati') # add a new element at any position in your list
print(motorcycles)

del motorcycles[0] 
print(motorcycles)

last_owned = motorcycles.pop() 
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove('ducati')
print(motorcycles)
