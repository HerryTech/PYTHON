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

motorcycles.insert(1, 'ducati')
print(motorcycles)
