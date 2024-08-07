# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check 
# whether a string is in the dictionary.
# www.py4e.com/code3/words.txt
#

words = list() # list of words of a parsed line
#uwords = list() # list of unique words
d = dict() # dictionary of keys (unique words from words.txt)
i = 0 # counter for unique words, use a value for dictionary keys 
count = 0 # counter for words read from words.txt

fhand = open('words.txt')

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        d[word] = d.get(word,0) + 1


print(d)
#print('======================================')
#print(f'Total words in words.txt: {count}')
#print(f'Unique words added to dictionary: {i}')
#print('======================================')
