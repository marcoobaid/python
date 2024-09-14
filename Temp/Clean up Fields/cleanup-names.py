### Read file containing cities and format all line as: City

# Open input file
fhand = open('city-input.txt')

# Convert input data to a list
cities = []
for city in fhand:
    city = city.lower().strip().capitalize()
    cities.append(city)

# Capitalize cities
capitalized_cities = [city.title() for city in cities]

# Dispaly resutls
for city in capitalized_cities: print(city)

