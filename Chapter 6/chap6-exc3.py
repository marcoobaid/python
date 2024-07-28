def count(string, letter):
    counter = 0
    for char in string:
        if char == letter:
            counter = counter + 1
    return counter

s = input('Enter a string: ')
l = input('What letter should I count? ')

result = count(s,l)

#print('\nI found', result, 'occurances of', l, 'in', s)

#sresult = str(result)
#print('\nI found ' + sresult + ' occurance(s) of "' + l + '" in "' + s + '"')

print(f'I found {result} occurances of "{l}" in the string "{s}"')
















  
