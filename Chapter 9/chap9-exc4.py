# Exercise 4: Add code to the above program to figure out who has the most messages 
# in the file. After all the data has been read and the dictionary has been created, 
# look through the dictionary using a maximum loop 
# (see Chapter 5: Maximum and minimum loops) to find who has the most messages and 
# print how many messages the person has.
# 
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# 
# Enter a file name: mbox.txt
# zqian@umich.edu 195
#
words = list()
emails = dict()

try:
    fhand = open(input('Enter a file name: '))
    #fhand = open('mbox-short.txt')
except:
    print('File does not exist! Try again :)')
    quit()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    emails[words[1]] = emails.get(words[1],0) + 1
    #print(words)
#print(emails)

largest = None
#for k in emails: # loop through keys
#    v = emails.get(k) # capture key value
for k,v in emails.items():
    if largest is None or v > largest:
        largest = v # largest value so far
        winner = k  # winnder key for largest vlaue

#print(winner, emails[winner])
print(winner, largest)

