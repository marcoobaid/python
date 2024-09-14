# Capitalize words within a list of addresses

fhand = open('addresses.txt')

for line in fhand:
    line = line.strip().lower().title()
    print(line)
    