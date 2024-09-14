def remove_duplicates(address_list):
    # Convert the list to a set (which automatically removes duplicates)
    unique_addresses = set(address_list)

    # Convert the set back to a list (if you need the result as a list)
    deduplicated_list = list(unique_addresses)

    return deduplicated_list

fhand = open('output.txt')
addresses = []

for line in fhand:
    line.strip()
    x = line.split(',')
    addresses.append(x[0].upper().rstrip())

# Example usage
if __name__ == "__main__":
    deduplicated_addresses = remove_duplicates(addresses)
    print("Deduplicated addresses:")
    # print list of unique addresses 
    for address in deduplicated_addresses:
        print(address)   
    
    # print count of unique addresses
    print(len(deduplicated_addresses))
    