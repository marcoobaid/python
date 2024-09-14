### Lookup site names based on a list of addresses

fhand = open('unique_addresses.txt')

# Generate a list of address to lookup their names
locations = []
for line in fhand:
    x = line.rstrip()
    locations.append(x.upper())

# Generate a dictionary of published directory
d = {}
fmaster = open('master-locations.csv')
for mline in fmaster:
    mline.strip().upper()
    y = mline.split(',')
    k = y[0].rstrip()
    v = y[1].rstrip()
    d[k] = v

# Find names of given list of addresses based on known dictionary
results = {}
for i in locations:
    # Lookup value (v) of a matched address (k)   
    for k,v in d.items():
        if i in k:
            results[i] = v
            break
        else:
            results[i] = 'None'

for k,v in results.items():
    print(f'{k},{v}')

print(f'********************************\n{len(results)} matches have been processed.')
print('Review results for accuracy!')

fhand.close()
fmaster.close()

