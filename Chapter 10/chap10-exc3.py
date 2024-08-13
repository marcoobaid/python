# Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages.
#  Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
#
import string

words = list()
counts = dict()

try:
    fhand = open(input('Enter a file name: '))
    #fhand = open('romeo.txt')
except:
    print('File does not exist! Try again :)')
    quit()

for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        letters = tuple(word)
        for l in letters:
            if l not in ['0', '1', '2', '3', '4' , '5', '6', '7', '8', '9']:
                counts[l] = counts.get(l,0) + 1

lst = sorted( [ (l,c) for (l,c) in counts.items()])

for l,c in lst:
    print(l,c)

