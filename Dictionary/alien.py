alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

users = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in users.items(): #key and value could be anything
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
for name in users.keys():
 print(f"\n{name.title()}")
 
for name in sorted(users.keys()):
 print(f"\n{name.title()}")