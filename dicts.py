states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

#Add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

#Print out some cities
print("-" * 10)
print("NY State has", cities["NY"])
print("OR State has", cities["OR"])

#Print out some states
print("-" * 10)
print("Michigan's abbreviation is:", states["Michigan"])
print("Florida's abbreviation is:", states["Florida"])

#Using the states then cities dicts
print("-" * 10)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])

#Print every states abbreviation
print("-" * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))
    
#Print every city in state
print("-" * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))
    
#Do both at the same time
print("-" * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

## safely get an abbreviation by state that might not be there
print("-" * 10)
state = states.get("Texas", None)
print(states)

if not state:
    print("Sorry, no Texas")
else:
    print("There is Texas")
    
# get a city with a default value
city = cities.get("TX", "Does not exist")
print("The city for the state 'TX' is: %s" % city)