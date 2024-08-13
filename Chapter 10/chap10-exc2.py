# Exercise 2: This program counts the distribution of the hour of the day for each of the 
# messages. You can pull the hour from the “From” line by finding the time string and 
# then splitting that string into parts using the colon character. Once you have 
# accumulated the counts for each hour, print out the counts, one per line, sorted by hour
#  as shown below.
# 
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# python timeofday.py
# Enter a file name: mbox-short.txt
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
#
words = list()
hours = dict()

try:
    fhand = open(input('Enter a file name: '))
except:
    print('File does not exist! Try again :)')
    quit()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    time = tuple(words[5]) # extract time
    hour = time[0] + time[1]
    hours[hour] = hours.get(hour,0) + 1

lst = sorted( [ (k,v) for k,v in hours.items() ], reverse=False )

for hr,ct in lst:
    print(hr,ct)
